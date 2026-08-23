import os
from flask import Flask, render_template, request, redirect, url_for, session, flash, send_from_directory
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = 'chave_secreta_planet_games_super_segura'

# Configuração de upload de capas
UPLOAD_FOLDER = os.path.join('static', 'capas')
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'webp'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Senha do Painel de Administração
ADMIN_PASSWORD = "planet123"

def arquivo_permitido(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

import os

import os

# ============================================================
# FUNÇÃO INTELIGENTE DE BUSCAR IMAGENS (HOME + CATÁLOGO)
# ============================================================
import os

# ============================================================
# FUNÇÃO UNIFICADA DE BUSCA DE IMAGENS (PAINEL + HOME + X360)
# ============================================================
def buscar_imagem_static(nome_ou_id):
    if not nome_ou_id:
        return 'sem-capa.jpg'
        
    valor = str(nome_ou_id).strip()
    
    # 1. Se for link externo (http/https), retorna o link puro
    if valor.startswith(('http://', 'https://')):
        return valor

    pasta_static = os.path.join(app.root_path, 'static')
    extensoes = ['.jpg', '.png', '.jpeg', '.webp', '.gif', '.JPG', '.PNG', '.WEBP']

    # 2. TESTA SE É UMA CAPA MANUAL DO PAINEL (Ex: "Castlevania.webp" em static/ ou static/capas/)
    for ext in ['', '.jpg', '.png', '.jpeg', '.webp']:
        teste = f"{valor}{ext}" if not valor.lower().endswith(('.jpg', '.png', '.jpeg', '.webp', '.gif')) else valor
        
        # Procura em static/capas/
        if os.path.isfile(os.path.join(pasta_static, 'capas', teste)):
            return f"capas/{teste}"
            
        # Procura solto em static/
        if os.path.isfile(os.path.join(pasta_static, teste)):
            return teste

    # 3. TESTA SE É ID DO XBOX 360 DENTRO DE static/x360db-main/titles/ID/artwork/boxart.*
    id_upper = valor.upper()
    for ext in extensoes:
        rel_artwork = f"x360db-main/titles/{id_upper}/artwork/boxart{ext}"
        if os.path.isfile(os.path.join(pasta_static, rel_artwork)):
            return rel_artwork

    # 4. TESTA SE O ID ESTÁ DIRETO EM static/x360db-main/titles/ID/boxart.*
    for ext in extensoes:
        rel_direto = f"x360db-main/titles/{id_upper}/boxart{ext}"
        if os.path.isfile(os.path.join(pasta_static, rel_direto)):
            return rel_direto

    return 'sem-capa.jpg'

# ============================================================
# 1. ROTA DA PÁGINA INICIAL
# ============================================================
@app.route('/')
def index():
    anuncios = [] # Ou a sua lógica para carregar anúncios
    return render_template('index.html', anuncios=anuncios)

# ============================================================
# 2. ROTA DA PÁGINA DE JOGOS
# ============================================================

lista_de_jogos = [
    {
        "id": 1,
        "titulo": "GodStix",
        "plataforma": "Xbox 360 - Formato: XEX",
        "tamanho": "30 MB",
        "categoria": "app",
        "imagem": "logo menor godstix.jpeg",
        "link": "https://4br.me/bkeFbDgA",
        "video": "https://www.youtube.com/watch?v=Wt01fROQNUM"
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


    },
    {
        "id": 19,
        "titulo": "Call of Duty Black Ops.rar",
        "plataforma": "Xbox 360 - Formato: XEX",
        "tamanho": "6.460 GB",
        "categoria": "acao",
        "imagem": "boxart.jpg",
        "link": "https://planetgames.net.br/download/Call%20of%20Duty%20Black%20Ops.rar"


    }


]

@app.route("/jogos")
def jogos():
    jogos_processados = []
    for j in lista_de_jogos:
        j_copy = dict(j)
        j_copy["imagem"] = buscar_imagem_static(j.get("imagem", ""))
        jogos_processados.append(j_copy)

    return render_template("jogos.html", jogos=jogos_processados)


@app.route("/xboxclassico")
def xboxclassico():
    jogos_processados = []
    
    # Substitua 'lista_de_jogos' pela sua lista contendo os jogos do Xbox Clássico
    for j in lista_de_jogos: 
        j_copy = dict(j)
        j_copy["imagem"] = buscar_imagem_static(j.get("imagem", ""))
        jogos_processados.append(j_copy)

    # Nome exato do arquivo que está na sua pasta templates:
    return render_template("xboxclassico.html", jogos=jogos_processados)



# ============================================================
# ROTA DO BATE-PAPO
# ============================================================
@app.route("/chat")   
def chat():
    return render_template("chat.html")


# ============================================================
# 3. ROTA DA PÁGINA DE PRODUTOS
# ============================================================
@app.route("/produtos")
def produtos():
    meus_anuncios = [
        {
            "ml_id": "MLB3666157348",
            "titulo": "Xbox 360 RGH 120GB + 20 Jogos",
            "preco": "R$ 1.490,00",
            "imagem": "xbox360 call of duty.webp",
            "link_ml": "https://www.mercadolivre.com.br/xbox-360-fat-super-elite-call-of-duty-rgh/up/MLBU3666157348" 
        },
        {
            "ml_id": "MLB4128396704",
            "titulo": "Estação De Retrabalho Reballing Bga Laser 10000 (Usado)",
            "preco": "R$ 3.500,00",
            "imagem": "D_NQ_NP_2X_815419-MLB110019916669_042026-F-estacao-de-retrabalho-reballing-bga-laser-10000.webp",
            "link_ml": "https://www.mercadolivre.com.br/estacao-de-retrabalho-reballing-bga-laser-10000/up/MLBU4128396704" 
        },
        {
            "ml_id": "MLB52897777",
            "titulo": "Console Sony Playstation 5 Edição Slim Disk 1tb Branco",
            "preco": "R$ 4.799,00",
            "imagem": "Console Sony Playstation 5 Edição Slim Disk 1tb Branco.webp",
            "link_ml": "https://www.mercadolivre.com.br/console-sony-playstation-5-edicao-slim-disk-1tb-branco-controle-sem-fio-dualsense-ps5-branco/p/MLB52897777"
        },
        {
            "ml_id": "MLB16268160",
            "titulo": "Controle Xbox Wireless",
            "preco": "R$ 453,00",
            "imagem": "Controle Xbox Wireless.webp",
            "link_ml": "https://www.mercadolivre.com.br/controle-xbox-wireless-series-xs-carbon-black/p/MLB16268160"
        },
        {
            "ml_id": "MLB5111737986",
            "titulo": "Bateria Controle Para Xbox Séries S X 1200mah Cabo 3m",
            "preco": "R$ 64,99",
            "imagem": "Bateria Controle Para Xbox Séries S X 1200mah Cabo 3m.webp",
            "link_ml": "https://www.mercadolivre.com.br/bateria-controle-para-xbox-series-s-x-1200mah-cabo-3m/up/MLBU2183606506?pdp_filters=item_id%3AMLB5111737986" 
        },
        {
            "ml_id": "MLB6737836486",
            "titulo": "Adaptador Videogame Game Stick M15 2 Controles Game Stick",
            "preco": "R$ 189,90",
            "imagem": "Adaptador Videogame Game Stick M15 2 Controles Game Stick.webp",
            "link_ml": "https://www.mercadolivre.com.br/adaptador-videogame-game-stick-m15-2-controles-game-stick/up/MLBU3956288428?pdp_filters=item_id%3AMLB6737836486"
        },
        {
            "ml_id": "MLB4111977276",
            "titulo": "Pc Gamer Completo I7 3.4ghz 16gb Ssd 480gb 500w Monitor 19",
            "preco": "R$ 2.026,58",
            "imagem": "Pc Gamer Completo I7 3.4ghz 16gb Ssd 480gb 500w Monitor 19.webp",
            "link_ml": "https://www.mercadolivre.com.br/pc-gamer-completo--i7-34ghz-16gb-ssd-480gb-500w-monitor-19/up/MLBU1986838950?pdp_filters=item_id%3AMLB4111977276"
        },
        {
            "ml_id": "MLB65916422",
            "titulo": "Smart TV 4K 50 LG Portal de Games Processador AI α7 Ger8 4K",
            "preco": "R$ 2.351,31",
            "imagem": "Smart TV 4K 50.webp",
            "link_ml": "https://www.mercadolivre.com.br/smart-tv-4k-50-lg-qned73-portal-de-games-processador-ai-7-ger8-4k-super-upscaling-google-cast-integrado-controle-ai-magic-webos-25-modo-esportes-alerta-de-esportes/p/MLB65916422"
        },
        {
            "ml_id": "MLB62709217",
            "titulo": "Bicicleta Elétrica Starmega V8 750W Preto",
            "preco": "R$ 5.930,15",
            "imagem": "Bicicleta Elétrica Starmega V8 750W Preto.webp",
            "link_ml": "https://www.mercadolivre.com.br/bicicleta-eletrica-starmega-v8-750w-preto-32kmh-bateria-48v-50km-autonomia/p/MLB62709217"
        },
        {
            "ml_id": "MLB68824482",
            "titulo": "Fonte Para Xbox 360 Slim Bivolt Conector 2 Pinos Com Cabo De Energia",
            "preco": "R$ 99,00",
            "imagem": "Fonte Para Xbox 360 Slim.webp",
            "link_ml": "https://www.mercadolivre.com.br/fonte-para-xbox-360-slim-bivolt-conector-2-pinos-com-cabo-de-energia-u-maisu/p/MLB68824482"
        }
       
    ]
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

@app.route("/admin")
def admin():
    if not session.get('admin_logged_in'):
        return redirect(url_for("admin_login"))
    return render_template("admin.html", jogos=lista_de_jogos)

@app.route("/admin/jogo/novo", methods=["POST"])
def novo_jogo():
    if not session.get('admin_logged_in'):
        return redirect(url_for("admin_login"))

    imagem_file = request.files.get("imagem_file")
    imagem_nome = request.form.get("imagem_url")

    if imagem_file and imagem_file.filename != '' and arquivo_permitido(imagem_file.filename):
        filename = secure_filename(imagem_file.filename)
        imagem_file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        imagem_nome = filename

    novo_id = max([j["id"] for j in lista_de_jogos], default=0) + 1
    lista_de_jogos.append({
        "id": novo_id,
        "titulo": request.form.get("titulo"),
        "plataforma": request.form.get("plataforma", "Xbox 360-Formato:XEX"),
        "tamanho": request.form.get("tamanho"),
        "categoria": request.form.get("categoria"),
        "imagem": imagem_nome if imagem_nome else "default.jpg",
        "link": request.form.get("link", "")
    })
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
        if imagem_file and imagem_file.filename != '' and arquivo_permitido(imagem_file.filename):
            filename = secure_filename(imagem_file.filename)
            imagem_file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            jogo["imagem"] = filename

    return redirect(url_for("admin"))

@app.route("/admin/jogo/excluir/<int:jogo_id>", methods=["POST"])
def excluir_jogo(jogo_id):
    if not session.get('admin_logged_in'):
        return redirect(url_for("admin_login"))

    global lista_de_jogos
    lista_de_jogos = [j for j in lista_de_jogos if j["id"] != jogo_id]
    return redirect(url_for("admin"))

import os
from flask import Flask, send_from_directory, abort

# ===================================================
# ROTAS DE DOWNLOAD DOS JOGOS
# ===================================================
import os
import json
from flask import render_template, request, current_app

@app.route('/catalogo-completo')
def catalogo_completo():
    try:
        page = request.args.get('page', 1, type=int)
        busca = request.args.get('busca', '', type=str).strip().lower()
        itens_por_pagina = 36

        # 1. Caminho correto do arquivo games.json na pasta static
        caminho_json = os.path.join(current_app.static_folder, 'x360db-main', 'games.json')
        
        todos_jogos = []
        if os.path.exists(caminho_json):
            with open(caminho_json, 'r', encoding='utf-8') as f:
                dados = json.load(f)
                # Adapta se o JSON for lista ou dicionário
                if isinstance(dados, list):
                    todos_jogos = dados
                elif isinstance(dados, dict):
                    todos_jogos = [{'id': k, 'nome': v.get('name', k) if isinstance(v, dict) else str(v)} for k, v in dados.items()]

        # 2. Filtro de Busca
        if busca:
            jogos_filtrados = [
                j for j in todos_jogos 
                if busca in str(j.get('name', j.get('nome', ''))).lower() 
                or busca in str(j.get('id', '')).lower()
            ]
        else:
            jogos_filtrados = todos_jogos

        # 3. Paginação Real (Garante alta velocidade)
        total_jogos = len(jogos_filtrados)
        total_paginas = (total_jogos + itens_por_pagina - 1) // itens_por_pagina if total_jogos > 0 else 1
        page = max(1, min(page, total_paginas))
        
        inicio = (page - 1) * itens_por_pagina
        fim = inicio + itens_por_pagina
        jogos_pagina = jogos_filtrados[inicio:fim]

        # 4. Formata a lista e valida as capas locais apenas dos 36 itens da página
        jogos_formatados = []
        for j in jogos_pagina:
            id_jogo = str(j.get('id', '')).strip()
            nome_jogo = j.get('name', j.get('nome', id_jogo))
            
            rel_artwork_jpg = f"x360db-main/titles/{id_jogo}/artwork/boxart.jpg"
            rel_artwork_png = f"x360db-main/titles/{id_jogo}/artwork/boxart.png"
            rel_boxart_jpg = f"x360db-main/titles/{id_jogo}/boxart.jpg"

            if os.path.exists(os.path.join(current_app.static_folder, rel_artwork_jpg)):
                capa = rel_artwork_jpg
            elif os.path.exists(os.path.join(current_app.static_folder, rel_artwork_png)):
                capa = rel_artwork_png
            elif os.path.exists(os.path.join(current_app.static_folder, rel_boxart_jpg)):
                capa = rel_boxart_jpg
            else:
                capa = "https://via.placeholder.com/200x240/12171a/ffffff?text=Sem+Capa"

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