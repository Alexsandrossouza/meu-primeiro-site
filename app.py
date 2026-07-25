import requests
from flask import Flask, render_template

app = Flask(__name__)

# ============================================================
# 1. ROTA DA PÁGINA INICIAL
# ============================================================
@app.route("/")
def index():
    return render_template("index.html")

# ============================================================
# 2. ROTA DA PÁGINA DE JOGOS (INTACTA)
# ============================================================
@app.route("/jogos")
def jogos():
    lista_de_jogos = [
        {
            "titulo": "GodStix",
            "plataforma": "Xbox 360 - Formato: XEX",
            "tamanho": "310 KB",
            "categoria": "app",
            "imagem": "logo menor godstix.jpeg",
            "link": "https://4br.me/godstix",
            "video": "https://www.youtube.com/watch?v=Wt01fROQNUM"
        },
        {
            "titulo": "Minecraft",
            "plataforma": "Xbox 360-Formato:XEX",
            "tamanho": "1.990 GB",
            "categoria": "rpg",
            "imagem": "Minecraft-Xbox-360-Edition.jpg",
            "link": "https://www.mediafire.com/file/nzhg7ertaij3o2w/M-X360-E-DLC-TU-XBLA.rar/file"
        },
        {
            "titulo": "Resident Evil Operation Raccoon City",
            "plataforma": "Xbox 360-Formato:XEX",
            "tamanho": "5.430 GB",
            "categoria": "terror",
            "imagem": "Resident-Evil-Operation-Raccoon-City-Special-Edition.jpg",
            "link": "https://www.mediafire.com/file/2a69bohl9wnzd2x/REORC-XEX.rar/file"
        },
        {   
            "titulo": "Grand Theft Auto V",
            "card-jogo": "acao",
            "plataforma": "Xbox 360-Formato:XEX",
            "tamanho": "16.5 GB",
            "categoria": "acao",
            "imagem": "Grand-Theft-Auto-V.jpg",
            "link_part1": "https://www.mediafire.com/file/k6j6g1xr7rz2ync/GTAV-XEX-DVD1yDVD2.part1.rar/file",
            "link_part2": "https://www.mediafire.com/file/1e6lll4a3m0d1me/GTAV-XEX-DVD1yDVD2.part2.rar/file"
        },
        {   
            "titulo": "Gears of War 3",
            "card-jogo": "acao",
            "plataforma": "Xbox 360-Formato:XEX",
            "tamanho": "7.5 GB",
            "categoria": "acao",
            "imagem": "Gears-of-War-3-scaled.jpg",
            "link": "https://www.mediafire.com/file/gzsi3qy0lnsu70o/G3%25E2%2588%2586R%2524_o_WIII_%2528TriploPlay_BR%2529.rar/file"
        },
        {
            "titulo": "Assassin's creed rogue",
            "plataforma": "Xbox 360-Formato:XEX",
            "tamanho": "5.58 GB",
            "categoria": "acao",
            "imagem": "Assassin's creed rogue.jpg",
            "link": "https://www.mediafire.com/file/b7c7ta1w0ok19g3/ACR-XEX.rar/file"
        },
        {
            "titulo": "Red Dead Redemption",
            "plataforma": "Xbox 360-Formato:XEX",
            "tamanho": "5.58 GB",
            "categoria": "acao",
            "imagem": "red-dead-redemption-game-of-the-year-edition-xbox-360-1_orig.jpg",
            "link_part1": "https://www.mediafire.com/file/6adboemuos4q8tu/lRIdF9u$UZh.part1.rar/file",
            "link_part2": "https://www.mediafire.com/file/1dh6q2hfdtqb2t3/lrIdF9u$UZh.part2.rar/file"
        },
        {
            "titulo": "Ace Combat 6 Fires Of Liberation",
            "plataforma": "Xbox 360-Formato:XEX",
            "tamanho": "4.74 GB",
            "categoria": "acao",
            "imagem": "ACE-6-X360-PackFront_FINAL.jpg",
            "link_part1": "https://www.mediafire.com/file/hdnsmo5dd9okdjp/Ace_Combat_6_AnDreXplay.part1.rar/file",
            "link_part2": "https://www.mediafire.com/file/1dh6q2hfdtqb2t3/lrIdF9u$UZh.part2.rar/file"
        }, 
        {
            "titulo": "Alice-Madness-Returns-X360 Senha:AnDrex",
            "plataforma": "Xbox 360-Formato:XEX",
            "tamanho": "2.1 / 2.1 GB",
            "categoria": "acao",
            "imagem": "Alice-Madness-Returns-X360.webp",
            "link_part1": "https://send.now/8ph8gtwv7on7",
            "link_part2": "https://send.now/7rxsxftbp9ia"
        },
        {
            "titulo": "skyrim",
            "plataforma": "Xbox 360-Formato:XEX",
            "tamanho": "4.36 GB",
            "categoria": "acao",
            "imagem": "skyrim.jpg",
            "link": "https://www.mediafire.com/file/iguca3f8nfnb71y/6%2525NBmVHwdPY%2526.rar/file"
        },
        {
            "titulo": "Horizon",
            "plataforma": "Xbox 360-Formato:XEX",
            "tamanho": "3.4 / 3.33 GB",
            "categoria": "corrida",
            "imagem": "horizon.jpg",
            "link_part1": "https://www.mediafire.com/file/8j9kyfwlbfinfzy/Forza_Horizon_AnDreXplay.part1.rar/file",
            "link_part2": "https://www.mediafire.com/file/472dfnbantnzpbb/Forza_Horizon_AnDreXplay.part2.rar/file"
        },
        {
            "titulo": "RESIDENT EVIL 6 BR Senha:RAFARGH6",
            "plataforma": "Xbox 360-Formato:XEX",
            "tamanho": "7,27 GB",
            "categoria": "terror",
            "imagem": "RESIDENT EVIL 6 BR.webp",
            "link": "https://4br.me/0zkNnxq61"
        },
        {
            "titulo": "Call of Duty Black Ops II",
            "plataforma": "Xbox 360-Formato:XEX",
            "tamanho": "3,9 / 3,3 GB",
            "categoria": "acao",
            "imagem": "Cover Call of Duty Black Ops II.webp",
            "link_part1": "https://4br.me/fQPWXmbK",
            "link_part2": "https://4br.me/BiU9BmkwJ"
        },
        {
            "titulo": "Lollipop Chainsaw",
            "plataforma": "Xbox 360-Formato:XEX",
            "tamanho": "5.1 GB",
            "categoria": "aventura",
            "imagem": "Cover_thumb.jpg",
            "link": "https://4br.me/p2xAlri9Lq"
        },
        {
            "titulo": "Far Cry 4",
            "plataforma": "Xbox 360-Formato:XEX",
            "tamanho": "6,7 GB",
            "categoria": "acao",
            "imagem": "Far Cry 4.webp",
            "link": "https://4br.me/U0ym4hWyZg"
        },
        {
            "titulo": "EMULADOR MEGA DRIVE + 1.071 ROMS",
            "plataforma": "Xbox 360-Formato:XEX",
            "tamanho": "739 MB",
            "categoria": "emulador",
            "imagem": "mega driver.png",
            "link": "https://4br.me/h1OfcxAMh"
        },
        {
            "titulo": "Emulador Super Nintendo + 3247 ROMS",
            "plataforma": "Xbox 360-Formato:XEX",
            "tamanho": "2.6 GB",
            "categoria": "emulador",
            "imagem": "emulador super nintendo.png",
            "link": "https://4br.me/gWP9d"
        },
        {
            "titulo": "Castlevania",
            "plataforma": "Xbox 360-Formato:XEX",
            "tamanho": "3.92 GB",
            "categoria": "aventura",
            "imagem": "Castlevania.webp",
            "link": "https://4br.me/mxjceVgp"
        }
    ]
    return render_template("jogos.html", jogos=lista_de_jogos)

# ============================================================
# 3. ROTA DA PÁGINA DE PRODUTOS (COM BUSCA AUTOMÁTICA DE PREÇO)
# ============================================================
@app.route("/produtos")
def produtos():
    meus_anuncios = [
        {
            "ml_id": "MLB54963150", # <--- Adicionado o ID do produto no ML
            "titulo": "Console Playstation 5 Slim Edição Digital 825 Gb",
            "preco": "R$ 5.999", # Valor padrão (será substituído se a API responder)
            "imagem": "Console Playstation 5 Slim Edição Digital 825 Gb.webp",
            "link_ml": "https://www.mercadolivre.com.br/console-playstation-5-slim-edicao-digital-825-gb/p/MLB54963150"
        },
        {
            "ml_id": "MLB3666157348",
            "titulo": "Xbox 360 RGH 120GB + 20 Jogos",
            "preco": "R$ 1490,00",
            "imagem": "xbox360 call of duty.webp",
            "link_ml": "https://www.mercadolivre.com.br/xbox-360-fat-super-elite-call-of-duty-rgh/up/MLBU3666157348" 
        },
        {
            "ml_id": "MLB4391533258",
            "titulo": "Dynavision3",
            "preco": "R$ 1000,00",
            "imagem": "Dynavision3.webp",
            "link_ml": "https://www.mercadolivre.com.br/dynavision-3/up/MLBU4391533258"
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
            "preco": "R$ 4.799",
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
            "preco": "R$ 58,99",
            "imagem": "Bateria Controle Para Xbox Séries S X 1200mah Cabo 3m.webp",
            "link_ml": "https://www.mercadolivre.com.br/bateria-controle-para-xbox-series-s-x-1200mah-cabo-3m/up/MLBU2183606506?pdp_filters=item_id%3AMLB5111737986" 
        },
        {
            "ml_id": "MLBU3956288428",
            "titulo": "Adaptador Videogame Game Stick M15 2 Controles Game Stick",
            "preco": "R$ 189,90",
            "imagem": "Adaptador Videogame Game Stick M15 2 Controles Game Stick.webp",
            "link_ml": "https://www.mercadolivre.com.br/adaptador-videogame-game-stick-m15-2-controles-game-stick/up/MLBU3956288428?pdp_filters=item_id%3AMLB6737836486"
        },
        {
            "ml_id": "MLB4111977276",
            "titulo": "Pc Gamer Completo I7 3.4ghz 16gb Ssd 480gb 500w Monitor 19",
            "preco": "R$ 2026,58",
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

    # --- LÓGICA QUE BUSCA OS PREÇOS NA API SEM ALTERAR O HTML OU APARÊNCIA ---
    for item in meus_anuncios:
        if "ml_id" in item:
            try:
                # Consulta a API oficial do Mercado Livre
                url = f"https://api.mercadolibre.com/items/{item['ml_id']}"
                resposta = requests.get(url, timeout=3)
                
                if resposta.status_code == 200:
                    dados = resposta.json()
                    preco_atual = dados.get("price")
                    if preco_atual:
                        # Atualiza o preço formatado em Real (ex: R$ 453.00)
                        item["preco"] = f"R$ {preco_atual:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
            except Exception:
                pass # Se falhar ou demorar, mantém o preço fixo digitado no dicionário

    return render_template("produtos.html", anuncios=meus_anuncios)