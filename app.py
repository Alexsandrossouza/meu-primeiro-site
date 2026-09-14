from pathlib import Path
import os
import json
import csv
from flask import Flask, render_template, request, redirect, url_for, session, flash, send_from_directory, jsonify
from werkzeug.utils import secure_filename
import sqlite3
from urllib.parse import quote, unquote, urlparse
import re
from difflib import SequenceMatcher

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY")

# Arquivo permanente onde os jogos cadastrados pelo Admin ficam salvos
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FOLDER = os.path.join(BASE_DIR, 'dados')
JOGOS_FILE = os.path.join(DATA_FOLDER, 'jogos.json')
os.makedirs(DATA_FOLDER, exist_ok=True)

# CSV DE REFERÊNCIA DO XBOX CLÁSSICO
CSV_XBOX = os.path.join(BASE_DIR, "renomeacao_xbox_classico.csv")

def carregar_ids_xbox():
    ids = {}

    if not os.path.isfile(CSV_XBOX):
        return ids

    with open(CSV_XBOX, "r", encoding="utf-8-sig", newline="") as arquivo:
        leitor = csv.DictReader(arquivo)

        for linha in leitor:
            nome_antigo = linha.get("Nome antigo", "").strip()
            nome_novo = linha.get("Nome novo", "").strip()

            if nome_antigo and nome_novo:
                chave = os.path.splitext(nome_novo)[0].lower()
                chave = re.sub(r"[^a-z0-9]+", " ", chave).strip()
                ids[chave] = os.path.splitext(nome_antigo)[0]

    return ids

# Configuração de upload de capas
UPLOAD_FOLDER = os.path.join('static', 'capas')
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'webp'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Senha do Painel de Administração
ADMIN_PASSWORD = os.environ.get("ADMIN_PASSWORD")

def arquivo_permitido(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# ============================================================
# FUNÇÃO INTELIGENTE DE BUSCAR IMAGENS NA PASTA STATIC
# ============================================================
def buscar_imagem_static(nome_imagem):
    if not nome_imagem:
        return 'sem-capa.jpg'
        
    if nome_imagem.startswith('http://') or nome_imagem.startswith('https://'):
        return nome_imagem

    nome_base = os.path.splitext(nome_imagem)[0]
    extensoes = ['.jpg', '.jpeg', '.png', '.webp', '.gif', '.JPG', '.PNG', '.WEBP']
    pasta_static = os.path.join(app.root_path, 'static')

    for ext in extensoes:
        arquivo_teste = f"{nome_base}{ext}"
        caminho_completo = os.path.join(pasta_static, arquivo_teste)
        if os.path.isfile(caminho_completo):
            return arquivo_teste

    return nome_imagem

# ============================================================
# 1. ROTA DA PÁGINA INICIAL
# ============================================================
@app.route("/")
def index():
    return render_template("index.html")

# ============================================================
# 2. ROTA DA PÁGINA DE JOGOS
# ============================================================

lista_inicial_de_jogos = [
    {
        "id": 1,
        "titulo": "GodStix",
        "plataforma": "Xbox 360 - Formato: XEX",
        "tamanho": "5 MB",
        "categoria": "app",
        "imagem": "GodStix.PNG",
        "link": "https://4br.me/CBlm2IaOKT",
        "video": "https://youtu.be/MzQx0dNSXc8"
    },
    {
       "id": 1,
       "titulo": "Dash_Launch_v3.21.7",
       "plataforma": "Xbox 360 - Formato: XEX",
       "tamanho": "1.60 MB",
       "categoria": "app",
       "imagem": "Dash_Launch_v3.21.jpg",
       "link": "https://consolemods.org/wiki/images/f/fd/Dash_Launch_v3.21.7z",
       
    },
    {
        "id": 1,
        "titulo": "XeXmenu_1.2",
        "plataforma": "Xbox 360 - Formato: XEX",
        "tamanho": "104 MB",
        "categoria": "app",
        "imagem": "watermarked_img_10289782803069378499.jpg",
        "link": "https://consolemods.org/wiki/images/5/5c/XeXmenu_1.2.7z",
        
    },
    {
        "id": 2,
        "titulo": "Minecraft",
        "plataforma": "Xbox 360 - Formato: XEX",
        "tamanho": "1.990 GB",
        "categoria": "rpg",
        "imagem": "Minecraft-Xbox-360-Edition.jpg",
        "link": "https://www.mediafire.com/file/nzhg7ertaij3o2w/M-X360-E-DLC-TU-XBLA.rar/file"
    },
    {
        "id": 3,
        "titulo": "Resident Evil Operation Raccoon City",
        "plataforma": "Xbox 360 - Formato: XEX",
        "tamanho": "5.430 GB",
        "categoria": "terror",
        "imagem": "Resident-Evil-Operation-Raccoon-City-Special-Edition.jpg",
        "link": "https://www.mediafire.com/file/2a69bohl9wnzd2x/REORC-XEX.rar/file"
    },
    {   
        "id": 4,
        "titulo": "Grand Theft Auto V",
        "plataforma": "Xbox 360 - Formato: XEX",
        "tamanho": "16.5 GB",
        "categoria": "acao",
        "imagem": "Grand-Theft-Auto-V.jpg",
        "link_part1": "https://www.mediafire.com/file/k6j6g1xr7rz2ync/GTAV-XEX-DVD1yDVD2.part1.rar/file",
        "link_part2": "https://www.mediafire.com/file/1e6lll4a3m0d1me/GTAV-XEX-DVD1yDVD2.part2.rar/file"
    },
    {   
        "id": 5,
        "titulo": "Gears of War 3",
        "plataforma": "Xbox 360 - Formato: XEX",
        "tamanho": "7.5 GB",
        "categoria": "acao",
        "imagem": "Gears-of-War-3-scaled.jpg",
        "link": "https://www.mediafire.com/file/gzsi3qy0lnsu70o/G3%25E2%2588%2586R%2524_o_WIII_%2528TriploPlay_BR%2529.rar/file"
    },
    {
        "id": 6,
        "titulo": "Assassin's creed rogue",
        "plataforma": "Xbox 360 - Formato: XEX",
        "tamanho": "5.58 GB",
        "categoria": "acao",
        "imagem": "Assassin's creed rogue.jpg",
        "link": "https://www.mediafire.com/file/b7c7ta1w0ok19g3/ACR-XEX.rar/file"
    },
    {
        "id": 7,
        "titulo": "Red Dead Redemption",
        "plataforma": "Xbox 360 - Formato: XEX",
        "tamanho": "5.58 GB",
        "categoria": "acao",
        "imagem": "red-dead-redemption-game-of-the-year-edition-xbox-360-1_orig.jpg",
        "link_part1": "https://www.mediafire.com/file/6adboemuos4q8tu/lRIdF9u$UZh.part1.rar/file",
        "link_part2": "https://www.mediafire.com/file/1dh6q2hfdtqb2t3/lrIdF9u$UZh.part2.rar/file"
    },
    {
        "id": 8,
        "titulo": "Ace Combat 6 Fires Of Liberation",
        "plataforma": "Xbox 360 - Formato: XEX",
        "tamanho": "4.74 GB",
        "categoria": "acao",
        "imagem": "https://m.media-amazon.com/images/I/81xU2pE64dL._AC_SL1500_.jpg",
        "link_part1": "https://www.mediafire.com/file/hdnsmo5dd9okdjp/Ace_Combat_6_AnDreXplay.part1.rar/file",
        "link_part2": "https://www.mediafire.com/file/exemplo_ace_part2"
    }, 
    {
        "id": 9,
        "titulo": "Dead or Alive 4",
        "plataforma": "Xbox 360 - Formato: XEX",
        "tamanho": "4.7 GB",
        "categoria": "luta",
        "imagem": "https://m.media-amazon.com/images/I/51M39C0QJAL._AC_.jpg",
        "link": "https://www.mediafire.com/file/exemplo_dead_or_alive"
    },
    {
        "id": 10,
        "titulo": "Alice-Madness-Returns-X360 Senha:AnDrex",
        "plataforma": "Xbox 360 - Formato: XEX",
        "tamanho": "2.1 / 2.1 GB",
        "categoria": "acao",
        "imagem": "Alice-Madness-Returns-X360.webp",
        "link_part1": "https://send.now/8ph8gtwv7on7",
        "link_part2": "https://send.now/7rxsxftbp9ia"
    },
    {
        "id": 11,
        "titulo": "skyrim",
        "plataforma": "Xbox 360 - Formato: XEX",
        "tamanho": "4.36 GB",
        "categoria": "acao",
        "imagem": "skyrim.jpg",
        "link": "https://www.mediafire.com/file/iguca3f8nfnb71y/6%2525NBmVHwdPY%2526.rar/file"
    },
    {
        "id": 12,
        "titulo": "Horizon",
        "plataforma": "Xbox 360 - Formato: XEX",
        "tamanho": "3.4 / 3.33 GB",
        "categoria": "corrida",
        "imagem": "horizon.jpg",
        "link_part1": "https://www.mediafire.com/file/8j9kyfwlbfinfzy/Forza_Horizon_AnDreXplay.part1.rar/file",
        "link_part2": "https://www.mediafire.com/file/472dfnbantnzpbb/Forza_Horizon_AnDreXplay.part2.rar/file"
    },
    {
        "id": 13,
        "titulo": "RESIDENT EVIL 6 BR Senha:RAFARGH6",
        "plataforma": "Xbox 360 - Formato: XEX",
        "tamanho": "7,27 GB",
        "categoria": "terror",
        "imagem": "RESIDENT EVIL 6 BR.webp",
        "link": "https://4br.me/0zkNnxq61"
    },
    {
        "id": 14,
        "titulo": "Call of Duty Black Ops II",
        "plataforma": "Xbox 360 - Formato: XEX",
        "tamanho": "3,9 / 3,3 GB",
        "categoria": "acao",
        "imagem": "Cover Call of Duty Black Ops II.webp",
        "link_part1": "https://4br.me/fQPWXmbK",
        "link_part2": "https://4br.me/BiU9BmkwJ"
    },
    {
        "id": 15,
        "titulo": "Lollipop Chainsaw",
        "plataforma": "Xbox 360 - Formato: XEX",
        "tamanho": "5.1 GB",
        "categoria": "aventura",
        "imagem": "Cover_thumb.jpg",
        "link": "https://4br.me/p2xAlri9Lq"
    },
    {
        "id": 16,
        "titulo": "Far Cry 4",
        "plataforma": "Xbox 360 - Formato: XEX",
        "tamanho": "6,7 GB",
        "categoria": "acao",
        "imagem": "Far Cry 4.webp",
        "link": "https://4br.me/U0ym4hWyZg"
    },
    {
        "id": 17,
        "titulo": "EMULADOR MEGA DRIVE + 1.071 ROMS",
        "plataforma": "Xbox 360 - Formato: XEX",
        "tamanho": "739 MB",
        "categoria": "emulador",
        "imagem": "mega driver.png",
        "link": "https://4br.me/h1OfcxAMh"
    },
    {
        "id": 18,
        "titulo": "Emulador Super Nintendo + 3247 ROMS",
        "plataforma": "Xbox 360 - Formato: XEX",
        "tamanho": "2.6 GB",
        "categoria": "emulador",
        "imagem": "emulador super nintendo.png",
        "link": "https://4br.me/gWP9d"
    },
    {
        "id": 19,
        "titulo": "Castlevania",
        "plataforma": "Xbox 360 - Formato: XEX",
        "tamanho": "3.92 GB",
        "categoria": "aventura",
        "imagem": "Castlevania.webp",
        "link": "https://4br.me/mxjceVgp"


    }


]

# ============================================================
# PERSISTÊNCIA DOS JOGOS
# ============================================================
def normalizar_ids(jogos):
    """Garante que cada jogo tenha um ID único, inclusive os jogos antigos."""
    usados = set()
    ids_validos = []

    for jogo in jogos:
        try:
            jid = int(jogo.get("id"))
        except (TypeError, ValueError):
            jid = None

        if jid is not None and jid > 0 and jid not in usados:
            jogo["id"] = jid
            usados.add(jid)
            ids_validos.append(jid)
        else:
            jogo["id"] = None

    proximo_id = max(ids_validos, default=0) + 1
    for jogo in jogos:
        if jogo["id"] is None:
            jogo["id"] = proximo_id
            usados.add(proximo_id)
            proximo_id += 1

    return jogos


def salvar_jogos():
    """Salva a lista atual em disco de forma segura."""
    normalizar_ids(lista_de_jogos)
    arquivo_temp = JOGOS_FILE + '.tmp'

    with open(arquivo_temp, 'w', encoding='utf-8') as f:
        json.dump(lista_de_jogos, f, ensure_ascii=False, indent=4)

    os.replace(arquivo_temp, JOGOS_FILE)


def carregar_jogos():
    """Carrega os jogos salvos. Na primeira execução usa os jogos antigos do app.py."""
    if os.path.exists(JOGOS_FILE):
        try:
            with open(JOGOS_FILE, 'r', encoding='utf-8') as f:
                dados = json.load(f)

            if isinstance(dados, list):
                return normalizar_ids(dados)
        except (json.JSONDecodeError, OSError) as e:
            print(f"Aviso: não foi possível ler {JOGOS_FILE}: {e}")

    jogos_iniciais = [dict(j) for j in lista_inicial_de_jogos]
    normalizar_ids(jogos_iniciais)

    # Cria o arquivo pela primeira vez sem apagar os jogos que já estavam no app.py.
    with open(JOGOS_FILE, 'w', encoding='utf-8') as f:
        json.dump(jogos_iniciais, f, ensure_ascii=False, indent=4)

    return jogos_iniciais


lista_de_jogos = carregar_jogos()

# ============================================================
# SCANNER AUTOMÁTICO — XBOX 360
# ============================================================

PASTA_XBOX360 = "/mnt/hd2tb/Download/Xbox360"
EXTENSOES_XBOX360 = {".rar", ".7z", ".zip", ".iso"}

def descobrir_jogos_xbox360():
    """Lê os arquivos existentes na pasta Xbox 360."""
    pasta = Path(PASTA_XBOX360)

    if not pasta.exists():
        return []

    jogos = []

    for arquivo in sorted(pasta.iterdir(), key=lambda x: x.name.lower()):
        if not arquivo.is_file():
            continue

        if arquivo.suffix.lower() not in EXTENSOES_XBOX360:
            continue

        jogos.append({
            "arquivo": arquivo.name,
            "titulo": arquivo.stem,
            "plataforma": "Xbox 360",
            "caminho": str(arquivo)
        })

    return jogos


# ============================================================
# CONFIGURAÇÕES DO PAINEL ADMIN
# ============================================================

ADMIN_CONFIG_FILE = os.path.join(DATA_FOLDER, "admin_config.json")


def carregar_admin_config():
    """Carrega as configurações personalizadas do painel Admin."""
    try:
        with open(ADMIN_CONFIG_FILE, "r", encoding="utf-8") as f:
            dados = json.load(f)

        return dados if isinstance(dados, dict) else {}

    except (FileNotFoundError, json.JSONDecodeError, OSError):
        return {}


def salvar_admin_config(config):
    """Salva as configurações do Admin com segurança."""
    arquivo_temp = ADMIN_CONFIG_FILE + ".tmp"

    with open(arquivo_temp, "w", encoding="utf-8") as f:
        json.dump(config, f, ensure_ascii=False, indent=4)

    os.replace(arquivo_temp, ADMIN_CONFIG_FILE)





lista_de_jogos = carregar_jogos()


@app.route("/jogos")
def jogos():
    jogos_processados = []

    for j in lista_de_jogos:
        plataforma = str(j.get("plataforma", "")).lower()

        if "clássico" in plataforma or "classico" in plataforma:
            continue

        j_copy = dict(j)
        j_copy["imagem"] = buscar_imagem_static(j.get("imagem", ""))
        jogos_processados.append(j_copy)

    return render_template(
        "jogos.html",
        jogos=jogos_processados
    )


@app.route("/xboxclassico")
def xboxclassico():

    pasta_jogos = "/mnt/hd2tb/Download/xboxclassico"
    pasta_capas = "/mnt/hd2tb/Download/covers/xbox classico"

    extensoes_jogos = {".7z", ".zip", ".rar", ".iso"}
    extensoes_capas = {".jpg", ".jpeg", ".png", ".webp", ".gif"}

    jogos_processados = []
    ids_xbox = carregar_ids_xbox()

    def normalizar_nome(nome):
        nome = os.path.splitext(nome)[0].lower()
        nome = re.sub(r"\[[^\]]*\]", " ", nome)
        nome = re.sub(r"\([^)]*\)", " ", nome)
        nome = re.sub(
            r"\s*-\s*pal\s*-\s*[a-z]{3}\b",
            " ",
            nome,
            flags=re.IGNORECASE
        )
        nome = re.sub(r"[^a-z0-9]+", " ", nome)
        nome = re.sub(r"\s+", " ", nome).strip()
        return nome

    def descobrir_genero(nome):
        n = normalizar_nome(nome)

        regras = {
            "Corrida": [
                "need for speed", "burnout", "forza", "project gotham",
                "midnight club", "flatout", "nascar", "rally",
                "r racing", "crash nitro kart", "mx unleashed",
                "atv", "colin mcrae", "f1", "formula one"
            ],
            "Esporte": [
                "fifa", "winning eleven", "pro evolution soccer", "pes ",
                "nba", "nfl", "nhl", "mlb", "madden", "tony hawk",
                "ssx", "top spin", "virtua tennis", "wwe", "wwf",
                "fight night", "golf", "baseball", "football", "basketball"
            ],
            "Luta": [
                "dead or alive", "mortal kombat", "street fighter",
                "tekken", "soulcalibur", "soul calibur",
                "king of fighters", "king of fighter", "capcom vs",
                "marvel vs", "dragon ball z budokai", "dragon ball z sagas",
                "bloody roar", "wwe", "wwf"
            ],
            "RPG": [
                "final fantasy", "star wars knights",
                "knights of the old republic", "kotor", "elder scrolls",
                "morrowind", "fable", "jade empire", "baldur",
                "fallout", "dragon quest", "phantasy star", "sudeki"
            ],
            "Terror": [
                "resident evil", "silent hill", "fatal frame",
                "project zero", "alone in the dark", "doom",
                "the suffering", "manhunt", "cold fear", "call of cthulhu"
            ],
            "Simulador": [
                "the sims", "simpsons road rage", "rollercoaster",
                "roller coaster", "zoo tycoon", "tycoon",
                "flight simulator", "train simulator"
            ],
            "Aventura": [
                "tomb raider", "prince of persia", "indiana jones",
                "lego", "syberia", "broken sword", "psychonauts",
                "beyond good", "oddworld", "conker", "banjo",
                "crash bandicoot", "sphinx"
            ],
            "Ação": [
                "halo", "doom", "quake", "far cry", "splinter cell",
                "tom clancy", "ghost recon", "rainbow six",
                "grand theft auto", "gta", "max payne", "hitman",
                "metal slug", "contra", "ninja gaiden", "dead to rights",
                "mercenaries", "destroy all humans", "007",
                "agent under fire", "nightfire", "everything or nothing",
                "from russia with love", "spider man", "spiderman", "batman"
            ]
        }

        for genero, palavras in regras.items():
            for palavra in palavras:
                if palavra in n:
                    return genero

        return "Ação"

    # CAPAS
    capas = {}

    if os.path.isdir(pasta_capas):
        for arquivo in os.listdir(pasta_capas):
            caminho = os.path.join(pasta_capas, arquivo)

            if not os.path.isfile(caminho):
                continue

            nome, extensao = os.path.splitext(arquivo)

            if extensao.lower() not in extensoes_capas:
                continue

            chave = normalizar_nome(nome)

            if chave and chave not in capas:
                capas[chave] = arquivo

    # JOGOS
    if not os.path.isdir(pasta_jogos):
        print(f"Pasta de jogos não encontrada: {pasta_jogos}")
        return render_template("xboxclassico.html", jogos=[])

    arquivos_jogos = [
        arquivo
        for arquivo in os.listdir(pasta_jogos)
        if os.path.isfile(os.path.join(pasta_jogos, arquivo))
        and os.path.splitext(arquivo)[1].lower() in extensoes_jogos
    ]

    arquivos_jogos.sort(key=lambda x: x.lower())

    print(f"XBOX CLÁSSICO: {len(arquivos_jogos)} arquivos encontrados")

    # MONTA TODOS OS CARDS
    for indice, arquivo in enumerate(arquivos_jogos, start=1):

        caminho_arquivo = os.path.join(pasta_jogos, arquivo)
        nome_jogo = os.path.splitext(arquivo)[0].strip()

        # TAMANHO
        tamanho_bytes = os.path.getsize(caminho_arquivo)

        if tamanho_bytes >= 1024 ** 3:
            tamanho = f"{tamanho_bytes / (1024 ** 3):.2f} GB"
        elif tamanho_bytes >= 1024 ** 2:
            tamanho = f"{tamanho_bytes / (1024 ** 2):.2f} MB"
        elif tamanho_bytes >= 1024:
            tamanho = f"{tamanho_bytes / 1024:.2f} KB"
        else:
            tamanho = f"{tamanho_bytes} bytes"

        # NOME NORMALIZADO
        chave_jogo = normalizar_nome(nome_jogo)

        # ID XBOX
        id_xbox = ""

        for nome_csv, id_arquivo in ids_xbox.items():
            nome_csv_normalizado = normalizar_nome(nome_csv)

            if nome_csv_normalizado == chave_jogo:
                id_xbox = os.path.splitext(id_arquivo)[0]
                break

        # CAPA
        imagem = ""

        # Primeiro tenta nome exato
        if chave_jogo in capas:
            imagem = (
                "/capas/xbox-classico/"
                + quote(capas[chave_jogo])
            )

        # Se não encontrou, tenta correspondência segura
        if not imagem:
            palavras_jogo = set(chave_jogo.split())

            numeros_jogo = {
                p for p in palavras_jogo
                if any(c.isdigit() for c in p)
                or p in {"ii", "iii", "iv", "v"}
            }

            for chave_capa, arquivo_capa in capas.items():

                palavras_capa = set(chave_capa.split())

                if not palavras_jogo:
                    continue

                numeros_capa = {
                    p for p in palavras_capa
                    if any(c.isdigit() for c in p)
                    or p in {"ii", "iii", "iv", "v"}
                }

                if numeros_jogo != numeros_capa.intersection(numeros_jogo):
                    continue

                if palavras_jogo.issubset(palavras_capa):
                    imagem = (
                        "/capas/xbox-classico/"
                        + quote(arquivo_capa)
                    )
                    break

        # DOWNLOAD
        link_download = (
            "/download/xboxclassico/"
            + quote(arquivo)
        )

        # GÊNERO
        genero = descobrir_genero(nome_jogo)

        # JOGO
        jogo = {
            "id": indice,
            "titulo": nome_jogo,
            "id_xbox": id_xbox,
            "plataforma": "Xbox Clássico",
            "tamanho": tamanho,
            "categoria": genero,
            "genero": genero,
            "imagem": imagem,
            "link": link_download,
            "arquivo": arquivo
        }

        jogos_processados.append(jogo)

    print(f"XBOX CLÁSSICO: {len(jogos_processados)} jogos processados")

    return render_template(
        "xboxclassico.html",
        jogos=jogos_processados
    )

# ============================================================
# ROTA DO BATE-PAPO
# ============================================================
@app.route("/chat")   
def chat():
    return render_template("chat.html")

# ============================================================
# SISTEMA DE BATE-PAPO - PLANET GAMES
# ============================================================

CHAT_DB = "/mnt/hd2tb/meu-primeiro-site/chat.db"


def inicializar_chat():
    conn = sqlite3.connect(CHAT_DB)

    conn.execute("""
        CREATE TABLE IF NOT EXISTS mensagens_chat (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            tipo TEXT NOT NULL,
            mensagem TEXT NOT NULL,
            data_hora DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)

    conn.commit()
    conn.close()


# Inicializa o banco automaticamente
inicializar_chat()


# ------------------------------------------------------------
# BUSCAR MENSAGENS
# ------------------------------------------------------------

@app.route("/api/chat/mensagens", methods=["GET"])
def buscar_mensagens_chat():

    conn = sqlite3.connect(CHAT_DB)
    conn.row_factory = sqlite3.Row

    mensagens = conn.execute("""
        SELECT
            id,
            nome,
            tipo,
            mensagem,
            data_hora
        FROM mensagens_chat
        ORDER BY id DESC
        LIMIT 100
    """).fetchall()

    conn.close()

    resultado = []

    for mensagem in mensagens:
        resultado.append({
            "id": mensagem["id"],
            "nome": mensagem["nome"],
            "tipo": mensagem["tipo"],
            "mensagem": mensagem["mensagem"],
            "data_hora": mensagem["data_hora"]
        })

    return jsonify(resultado)


# ------------------------------------------------------------
# ENVIAR MENSAGEM
# ------------------------------------------------------------

@app.route("/api/chat/enviar", methods=["POST"])
def enviar_mensagem_chat():

    dados = request.get_json()

    if not dados:
        return jsonify({
            "erro": "Dados não enviados."
        }), 400

    nome = str(dados.get("nome", "")).strip()
    tipo = str(dados.get("tipo", "")).strip()
    mensagem = str(dados.get("mensagem", "")).strip()

    # Validação
    if not nome:
        return jsonify({
            "erro": "Digite seu nome."
        }), 400

    if not tipo:
        return jsonify({
            "erro": "Escolha o tipo da mensagem."
        }), 400

    if not mensagem:
        return jsonify({
            "erro": "Digite uma mensagem."
        }), 400

    # Limites de segurança
    nome = nome[:50]
    tipo = tipo[:50]
    mensagem = mensagem[:1000]

    conn = sqlite3.connect(CHAT_DB)

    conn.execute("""
        INSERT INTO mensagens_chat
        (nome, tipo, mensagem)
        VALUES (?, ?, ?)
    """, (
        nome,
        tipo,
        mensagem
    ))

    conn.commit()
    conn.close()

    return jsonify({
        "sucesso": True,
        "mensagem": "Mensagem enviada com sucesso!"
    })
        # ============================================================
        # EXCLUIR MENSAGEM DO BATE-PAPO
        # ============================================================

@app.route("/api/chat/excluir/<int:id>", methods=["DELETE"])
def excluir_mensagem_chat(id):
    try:
        conn = sqlite3.connect(CHAT_DB)

        cursor = conn.execute(
            "DELETE FROM mensagens_chat WHERE id = ?",
            (id,)
        )

        conn.commit()
        conn.close()

        if cursor.rowcount == 0:
            return jsonify({
                "sucesso": False,
                "erro": "Mensagem não encontrada."
            }), 404

        return jsonify({
            "sucesso": True,
            "mensagem": "Mensagem excluída com sucesso."
        })

    except Exception as e:
        return jsonify({
            "sucesso": False,
            "erro": str(e)
        }), 500


# ============================================================
# 3. ROTA DA PÁGINA DE PRODUTOS
# ============================================================
@app.route("/produtos")
def produtos():
    import json
    try:
        with open(os.path.join(DATA_FOLDER, "produtos.json"), "r", encoding="utf-8") as f:
            meus_anuncios = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        meus_anuncios = []
    return render_template("produtos.html", anuncios=meus_anuncios)


# ============================================================
# 4. ROTAS DO PAINEL ADMIN (SENHA, UPLOAD, EDIÇÃO E EXCLUSÃO)
# ============================================================
@app.route("/admin/login", methods=["GET", "POST"])
def admin_login():
    if request.method == "POST":
        senha = request.form.get("senha")
        if senha == ADMIN_PASSWORD:
            session['admin_logged_in'] = True
            return redirect(url_for("admin"))
        else:
            flash("Senha incorreta!")
    return render_template("admin_login.html")

@app.route("/admin/logout")
def admin_logout():
    session.pop('admin_logged_in', None)
    return redirect(url_for("admin_login"))


# ============================================================
# GERENCIAMENTO DE PRODUTOS - PAINEL ADMIN
# ============================================================

def carregar_produtos():
    arquivo = os.path.join(DATA_FOLDER, "produtos.json")

    try:
        with open(arquivo, "r", encoding="utf-8") as f:
            dados = json.load(f)

        return dados if isinstance(dados, list) else []

    except (FileNotFoundError, json.JSONDecodeError, OSError):
        return []


def salvar_produtos(produtos):
    arquivo = os.path.join(DATA_FOLDER, "produtos.json")
    arquivo_temp = arquivo + ".tmp"

    with open(arquivo_temp, "w", encoding="utf-8") as f:
        json.dump(produtos, f, ensure_ascii=False, indent=4)

    os.replace(arquivo_temp, arquivo)


@app.route("/admin/produto/novo", methods=["POST"])
def admin_produto_novo():
    if not session.get("admin_logged_in"):
        return redirect(url_for("admin_login"))

    produtos = carregar_produtos()

    produto = {
        "titulo": request.form.get("titulo", "").strip(),
        "imagem": request.form.get("imagem", "").strip(),
        "preco": request.form.get("preco", "").strip(),
        "link": request.form.get("link", "").strip(),
        "ativo": True
    }

    produtos.append(produto)
    salvar_produtos(produtos)

    flash("Produto adicionado com sucesso!")
    return redirect(url_for("admin"))


@app.route("/admin/produto/editar/<int:produto_id>", methods=["POST"])
def admin_produto_editar(produto_id):
    if not session.get("admin_logged_in"):
        return redirect(url_for("admin_login"))

    produtos = carregar_produtos()

    if produto_id < 0 or produto_id >= len(produtos):
        flash("Produto não encontrado.")
        return redirect(url_for("admin"))

    produto = produtos[produto_id]

    produto["titulo"] = request.form.get("titulo", "").strip()
    produto["imagem"] = request.form.get("imagem", "").strip()
    produto["preco"] = request.form.get("preco", "").strip()
    produto["link"] = request.form.get("link", "").strip()

    salvar_produtos(produtos)

    flash("Produto atualizado com sucesso!")
    return redirect(url_for("admin"))


@app.route("/admin/produto/excluir/<int:produto_id>", methods=["POST"])
def admin_produto_excluir(produto_id):
    if not session.get("admin_logged_in"):
        return redirect(url_for("admin_login"))

    produtos = carregar_produtos()

    if produto_id < 0 or produto_id >= len(produtos):
        flash("Produto não encontrado.")
        return redirect(url_for("admin"))

    produtos.pop(produto_id)
    salvar_produtos(produtos)

    flash("Produto removido com sucesso!")
    return redirect(url_for("admin"))


@app.route("/admin/produto/toggle/<int:produto_id>", methods=["POST"])
def admin_produto_toggle(produto_id):
    if not session.get("admin_logged_in"):
        return redirect(url_for("admin_login"))

    produtos = carregar_produtos()

    if produto_id < 0 or produto_id >= len(produtos):
        flash("Produto não encontrado.")
        return redirect(url_for("admin"))

    produto = produtos[produto_id]
    produto["ativo"] = not produto.get("ativo", True)

    salvar_produtos(produtos)

    return redirect(url_for("admin"))


@app.route("/admin")
def admin():
    if not session.get('admin_logged_in'):
        return redirect(url_for("admin_login"))
    jogos_xbox360 = descobrir_jogos_xbox360()
    produtos = carregar_produtos()

    return render_template(
        "admin.html",
        jogos=lista_de_jogos,
        jogos_xbox360=jogos_xbox360,
        produtos=produtos
    )
@app.route("/admin/jogo/novo", methods=["GET", "POST"])
def novo_jogo():

    if not session.get('admin_logged_in'):
        return redirect(url_for("admin_login"))

    if request.method == "GET":
        return render_template("novo_jogo.html")

    imagem_file = request.files.get("imagem_file")
    imagem_nome = request.form.get("imagem_url", "").strip()

    if imagem_file and imagem_file.filename != '' and arquivo_permitido(imagem_file.filename):
        filename = secure_filename(imagem_file.filename)
        imagem_file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        imagem_nome = filename

    # Se o Admin receber uma URL completa de uma capa do Xbox Clássico,
    # converte a URL de volta para o nome real do arquivo.
    # Exemplo:
    # https://planetgames.net.br/capas/xbox-classico/All-Star%20Baseball%20%2705.jpg
    # vira:
    # All-Star Baseball '05.jpg
    if imagem_nome.startswith(("http://", "https://")):
        caminho_url = urlparse(imagem_nome)

        # Para capas hospedadas no próprio Planet Games, salva somente
        # o nome real do arquivo. Isso permite gerar automaticamente
        # os %20 quando o nome possui espaços.
        if caminho_url.netloc == "planetgames.net.br":
            nome_url = os.path.basename(caminho_url.path)
            imagem_nome = unquote(nome_url)

    # ============================================================
    # DADOS DO JOGO
    # ============================================================

    titulo = request.form.get("titulo", "").strip()
    plataforma_form = request.form.get("plataforma", "").strip()
    arquivo_nome = request.form.get("arquivo", "").strip()
    categoria = request.form.get("categoria", "").strip()
    tamanho = request.form.get("tamanho", "").strip()

    # ============================================================
    # PLATAFORMA
    # ============================================================

    if plataforma_form == "Xbox 360":
        plataforma = "Xbox 360 - Formato: XEX"
        pasta_download = "/mnt/hd2tb/Download/Xbox360"
    else:
        plataforma = "Xbox Clássico"
        pasta_download = "/mnt/hd2tb/Download/xboxclassico"

    # ============================================================
    # TAMANHO AUTOMÁTICO DO ARQUIVO
    # ============================================================

    if arquivo_nome:

        caminho_arquivo = os.path.join(
            pasta_download,
            arquivo_nome
        )

        if os.path.isfile(caminho_arquivo):

            tamanho_bytes = os.path.getsize(caminho_arquivo)

            if tamanho_bytes >= 1024 ** 3:
                tamanho = f"{tamanho_bytes / (1024 ** 3):.2f} GB"

            elif tamanho_bytes >= 1024 ** 2:
                tamanho = f"{tamanho_bytes / (1024 ** 2):.2f} MB"

            elif tamanho_bytes >= 1024:
                tamanho = f"{tamanho_bytes / 1024:.2f} KB"

            else:
                tamanho = f"{tamanho_bytes} bytes"

    # ============================================================
    # ID
    # ============================================================

    novo_id = max(
        [j["id"] for j in lista_de_jogos],
        default=0
    ) + 1

    # ============================================================
    # LINK DO DOWNLOAD
    # ============================================================

    if arquivo_nome:

        link_download = (
            f"Xbox360/{arquivo_nome}"
            if plataforma_form == "Xbox 360"
            else f"xboxclassico/{arquivo_nome}"
        )

    else:

        link_download = request.form.get("link", "").strip()

    # ============================================================
    # CADASTRAR JOGO
    # ============================================================

    lista_de_jogos.append({

        "id": novo_id,

        "titulo": titulo,

        "plataforma": plataforma,

        "tamanho": tamanho,

        "categoria": categoria,

        "imagem": imagem_nome if imagem_nome else "default.jpg",

        "link": link_download

    })

    salvar_jogos()

    return redirect(url_for("admin"))

@app.route("/admin/jogo/editar/<int:jogo_id>", methods=["POST"])
def editar_jogo(jogo_id):
    if not session.get('admin_logged_in'):
        return redirect(url_for("admin_login"))

    jogo = next((j for j in lista_de_jogos if j["id"] == jogo_id), None)
    if jogo:
        jogo["titulo"] = request.form.get("titulo")
        jogo["plataforma"] = request.form.get("plataforma")
        jogo["tamanho"] = request.form.get("tamanho")
        jogo["categoria"] = request.form.get("categoria")
        if request.form.get("link"):
            jogo["link"] = request.form.get("link")

        imagem_file = request.files.get("imagem_file")
        imagem_url = request.form.get("imagem_url", "").strip()

        if imagem_file and imagem_file.filename != '' and arquivo_permitido(imagem_file.filename):
            filename = secure_filename(imagem_file.filename)
            imagem_file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            jogo["imagem"] = filename

        elif imagem_url:
            # Aceita tanto o nome do arquivo quanto a URL completa.
            # Se for uma URL do Planet Games, guarda apenas o nome real.
            if imagem_url.startswith(("http://", "https://")):
                caminho_url = urlparse(imagem_url)

                if caminho_url.netloc == "planetgames.net.br":
                    nome_url = os.path.basename(caminho_url.path)
                    jogo["imagem"] = unquote(nome_url)
                else:
                    jogo["imagem"] = imagem_url
            else:
                jogo["imagem"] = imagem_url

        salvar_jogos()

    return redirect(url_for("admin"))

@app.route("/admin/jogo/excluir/<int:jogo_id>", methods=["POST"])
def excluir_jogo(jogo_id):
    if not session.get('admin_logged_in'):
        return redirect(url_for("admin_login"))

    global lista_de_jogos
    lista_de_jogos = [j for j in lista_de_jogos if j["id"] != jogo_id]
    salvar_jogos()
    return redirect(url_for("admin"))

# ============================================================
# ROTAS DE DOWNLOAD
# ============================================================
# ============================================================
# ROTAS DE DOWNLOAD
# ============================================================
# ============================================================
# ROTAS DE DOWNLOAD
# ============================================================

@app.route('/download/')
@app.route('/download/<path:subpath>')
def listar_download(subpath=''):

    import os
    from flask import abort, send_from_directory

    caminho_base = '/mnt/hd2tb/Download'

    # Evita caminhos perigosos
    subpath = subpath.replace('\\', '/').lstrip('/')

    caminho = os.path.normpath(
        os.path.join(caminho_base, subpath)
    )

    # Impede sair da pasta Download
    if not caminho.startswith(os.path.normpath(caminho_base)):
        abort(403)

    if not os.path.exists(caminho):
        abort(404)

    # Se for arquivo, envia para download
    if os.path.isfile(caminho):

        return send_from_directory(
            os.path.dirname(caminho),
            os.path.basename(caminho),
            as_attachment=True
        )

    # Se for pasta, lista os arquivos
    arquivos = os.listdir(caminho)

    html = f"<h1>Conteúdo de /Download/{subpath}</h1><ul>"

    for f in arquivos:

        caminho_item = os.path.join(caminho, f)

        link = f"/download/{subpath}/{f}" if subpath else f"/download/{f}"

        if os.path.isdir(caminho_item):
            html += f'<li>📁 <a href="{link}">{f}</a></li>'
        else:
            html += f'<li>📦 <a href="{link}">{f}</a></li>'

    html += "</ul>"

    return html

# ============================================================
# ROTAS DE DOWNLOAD   FIM
# ============================================================

@app.route('/capas/xbox-classico/<path:nome>')
def servir_capa_xbox_classico(nome):
    pasta_covers = '/mnt/hd2tb/Download/covers/xbox classico'

    # Flask entrega o parâmetro já decodificado em muitos casos.
    # unquote também protege contra URLs que ainda estejam percent-encoded.
    nome = unquote(nome)

    return send_from_directory(pasta_covers, nome)

@app.route('/catalogo-completo')
def catalogo_completo():
    try:
        page = request.args.get('page', 1, type=int)
        busca = request.args.get('busca', '', type=str).strip().lower()
        itens_por_pagina = 36

        caminho_json = os.path.join(app.static_folder, 'x360db-main', 'games.json')
        
        todos_jogos = []
        if os.path.exists(caminho_json):
            with open(caminho_json, 'r', encoding='utf-8') as f:
                dados = json.load(f)
                if isinstance(dados, list):
                    todos_jogos = dados
                elif isinstance(dados, dict):
                    todos_jogos = [{'id': k, 'nome': v.get('name', v.get('title', k)) if isinstance(v, dict) else str(v)} for k, v in dados.items()]

        # Busca corrigida: verifica tanto 'nome' quanto 'name' e 'id'
        if busca:
            jogos_filtrados = []
            for j in todos_jogos:
                nome_jogo = str(j.get('nome', j.get('name', j.get('title', '')))).lower()
                id_jogo = str(j.get('id', '')).lower()
                if busca in nome_jogo or busca in id_jogo:
                    jogos_filtrados.append(j)
        else:
            jogos_filtrados = todos_jogos

        # Paginação
        total_jogos = len(jogos_filtrados)
        total_paginas = (total_jogos + itens_por_pagina - 1) // itens_por_pagina if total_jogos > 0 else 1
        page = max(1, min(page, total_paginas))
        
        inicio = (page - 1) * itens_por_pagina
        fim = inicio + itens_por_pagina
        jogos_pagina = jogos_filtrados[inicio:fim]

        jogos_formatados = []

        for j in jogos_pagina:

            id_jogo = str(j.get('id', '')).strip()

            nome_jogo = j.get(
                'nome',
                j.get(
                    'name',
                    j.get('title', id_jogo)
                )
            )

            # ====================================================
            # CAPA XBOX 360 - X360DB
            # ====================================================

            rel_artwork_jpg = (
                f"x360db-main/titles/{id_jogo}/artwork/boxart.jpg"
            )

            rel_artwork_png = (
                f"x360db-main/titles/{id_jogo}/artwork/boxart.png"
            )

            rel_boxart_jpg = (
                f"x360db-main/titles/{id_jogo}/boxart.jpg"
            )

            if os.path.exists(
                os.path.join(
                    app.static_folder,
                    rel_artwork_jpg
                )
            ):

                capa = rel_artwork_jpg

            elif os.path.exists(
                os.path.join(
                    app.static_folder,
                    rel_artwork_png
                )
            ):

                capa = rel_artwork_png

            elif os.path.exists(
                os.path.join(
                    app.static_folder,
                    rel_boxart_jpg
                )
            ):

                capa = rel_boxart_jpg

            else:

                capa = None

            jogos_formatados.append({
                'id': id_jogo,
                'nome': nome_jogo,
                'capa': capa
            })

        return render_template(
            'catalogo_x360db.html',
            jogos=jogos_formatados,
            page=page,
            total_paginas=total_paginas,
            busca=busca
        )
    except Exception as e:
        print(f"Erro no catálogo: {e}")
        return f"Erro interno ao carregar o catálogo: {e}", 500


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=False)