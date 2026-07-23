from flask import Flask, render_template

app = Flask(__name__)

# ============================================================
# 1. ROTA DA PÁGINA INICIAL
# ============================================================
@app.route("/")
def index():
    return render_template("index.html")

# ============================================================
# 2. ROTA DA PÁGINA DE JOGOS
# ============================================================
@app.route("/jogos")
def jogos():
    lista_de_jogos = [
        {
        "titulo": "GodStix",
        "plataforma": "Xbox 360 - Formato: XEX",
        "tamanho": "310 MB",
        "imagem": "logo menor godstix.jpeg",
        "link": "https://4br.me/godstix"
        },
        {
            "titulo": "Minecraft",
            "plataforma": "Xbox 360-Formato:XEX",
            "tamanho": "1.990 GB",
            "imagem": "Minecraft-Xbox-360-Edition.jpg",
            "link": "https://www.mediafire.com/file/nzhg7ertaij3o2w/M-X360-E-DLC-TU-XBLA.rar/file"
        },
        {
            "titulo": "Resident Evil Operation Raccoon City",
            "plataforma": "Xbox 360-Formato:XEX",
            "tamanho": "5.430 GB",
            "imagem": "Resident-Evil-Operation-Raccoon-City-Special-Edition.jpg",
            "link": "https://www.mediafire.com/file/2a69bohl9wnzd2x/REORC-XEX.rar/file"
        },
        {
            "titulo": "Grand Theft Auto V",
            "plataforma": "Xbox 360-Formato:XEX",
            "tamanho": "16.5 GB",
            "imagem": "Grand-Theft-Auto-V.jpg",
            "link_part1": "https://www.mediafire.com/file/k6j6g1xr7rz2ync/GTAV-XEX-DVD1yDVD2.part1.rar/file",
            "link_part2": "https://www.mediafire.com/file/1e6lll4a3m0d1me/GTAV-XEX-DVD1yDVD2.part2.rar/file"
        },
        {
            "titulo": "Gears of War 3",
            "plataforma": "Xbox 360-Formato:XEX",
            "tamanho": "7.5 GB",
            "imagem": "Gears-of-War-3-scaled.jpg",
            "link": "https://www.mediafire.com/file/gzsi3qy0lnsu70o/G3%25E2%2588%2586R%2524_o_WIII_%2528TriploPlay_BR%2529.rar/file"
        },
        {
            "titulo": "Assassin's creed rogue",
            "plataforma": "Xbox 360-Formato:XEX",
            "tamanho": "5.58 GB",
            "imagem": "Assassin's creed rogue.jpg",
            "link": "https://www.mediafire.com/file/b7c7ta1w0ok19g3/ACR-XEX.rar/file"
            
        },
        {
            "titulo": "Red Dead Redemption",
            "plataforma": "Xbox 360-Formato:XEX",
            "tamanho": "5.58 GB",
            "imagem": "red-dead-redemption-game-of-the-year-edition-xbox-360-1_orig.jpg",
            "link_part1": "https://www.mediafire.com/file/6adboemuos4q8tu/lRIdF9u$UZh.part1.rar/file",
            "link_part2": "https://www.mediafire.com/file/1dh6q2hfdtqb2t3/lrIdF9u$UZh.part2.rar/file"
        },
        {
            "titulo": "Ace Combat 6 Fires Of Liberation",
            "plataforma": "Xbox 360-Formato:XEX",
            "tamanho": "4.74 GB",
            "imagem": "ACE-6-X360-PackFront_FINAL.jpg",
            "link_part1": "https://www.mediafire.com/file/hdnsmo5dd9okdjp/Ace_Combat_6_AnDreXplay.part1.rar/file",
            "link_part2": "https://www.mediafire.com/file/1dh6q2hfdtqb2t3/lrIdF9u$UZh.part2.rar/file"
        
        }, 
        {
            "titulo": "Alice-Madness-Returns-X360",
            "plataforma": "Xbox 360-Formato:XEX",
            "tamanho": "2.1 / 2.1 GB",
            "imagem": "Alice-Madness-Returns-X360.webp",
            "link_part1": "https://send.now/8ph8gtwv7on7",
            "link_part2": "https://send.now/7rxsxftbp9ia"
        },
        {
            "titulo": "skyrim",
            "plataforma": "Xbox 360-Formato:XEX",
            "tamanho": "4.36 GB",
            "imagem": "skyrim.jpg",
            "link": "https://www.mediafire.com/file/iguca3f8nfnb71y/6%2525NBmVHwdPY%2526.rar/file"
        },
        {
            "titulo": "Assassin's Creed Rogue",
            "plataforma": "Xbox 360-Formato:XEX",
            "tamanho": "7.5 GB",
            "imagem": "gears-of-war-3.jpg",
            "link": "https://produto.mercadolivre.com.br/MLB-LINK-GEARS"
        }
    ] # Fecha corretamente a lista_de_jogos
    
    return render_template("jogos.html", jogos=lista_de_jogos)

# ============================================================
# 3. ROTA DA PÁGINA DE PRODUTOS
# ============================================================
@app.route("/produtos")
def produtos():
    meus_anuncios = [
        {
            "titulo": "Xbox 360 RGH 120GB + 20 Jogos",
            "preco": "R$ 1490,00",
            "imagem": "xbox360 call of duty.webp",
            "link_ml": "https://www.mercadolivre.com.br/xbox-360-fat-super-elite-call-of-duty-rgh/up/MLBU3666157348" 
        },
        {
            "titulo": "Dynavision3",
            "preco": "R$ 1000,00",
            "imagem": "Dynavision3.webp",
            "link_ml": "https://www.mercadolivre.com.br/dynavision-3/up/MLBU4391533258"
        },
        {
            "titulo": "Estação De Retrabalho Reballing Bga Laser 10000 (Usado)",
            "preco": "R$ 3.500,00",
            "imagem": "D_NQ_NP_2X_815419-MLB110019916669_042026-F-estacao-de-retrabalho-reballing-bga-laser-10000.webp",
            "link_ml": "https://www.mercadolivre.com.br/estacao-de-retrabalho-reballing-bga-laser-10000/up/MLBU4128396704" 
        },
        {
            "titulo": "Controle Xbox Wireless",
            "preco": "R$ 449,00",
            "imagem": "Controle Xbox Wireless.webp",
            "link_ml": "https://meli.la/31BVKKm"
        },
        {
            "titulo": "Bateria Controle Para Xbox Séries S X 1200mah Cabo 3m",
            "preco": "R$ 58,99",
            "imagem": "Bateria Controle Para Xbox Séries S X 1200mah Cabo 3m.webp",
            "link_ml": "https://meli.la/1imnURo" 
        },
        {
            "titulo": "Adaptador Videogame Game Stick M15 2 Controles Game Stick",
            "preco": "R$ 189,90",
            "imagem": "Adaptador Videogame Game Stick M15 2 Controles Game Stick,webp",
            "link_ml": "https://meli.la/2HXaJs1"
        },
        {
            "titulo": "Pc Gamer Completo I7 3.4ghz 16gb Ssd 480gb 500w Monitor 19",
            "preco": "R$ 2026,58",
            "imagem": "Pc Gamer Completo I7 3.4ghz 16gb Ssd 480gb 500w Monitor 19.webp",
            "link_ml": "https://meli.la/1okF9RD"
        },
        {
            "titulo": "Logo mais novidades",
            "preco": "R$ 00,00",
            "imagem": "fundo.jpg.png",
            "link_ml": "https://mercadolivre.com.br"
        },
        {
            "titulo": "Logo mais novidades",
            "preco": "R$ 00,00",
            "imagem": "fundo.jpg.png",
            "link_ml": "https://mercadolivre.com.br"
        },
        {
            "titulo": "Logo mais novidades",
            "preco": "R$ 00,00",
            "imagem": "fundo.jpg.png",
            "link_ml": "https://mercadolivre.com.br"
        },
        {
            "titulo": "Logo mais novidades",
            "preco": "R$ 00,00",
            "imagem": "fundo.jpg.png",
            "link_ml": "https://mercadolivre.com.br"
        },
        {
            "titulo": "Logo mais novidades",
            "preco": "R$ 00,00",
            "imagem": "fundo.jpg.png",
            "link_ml": "https://mercadolivre.com.br"
        },
        {
            "titulo": "Logo mais novidades",
            "preco": "R$ 00,00",
            "imagem": "fundo.jpg.png",
            "link_ml": "https://mercadolivre.com.br"
        },
        {
            "titulo": "Logo mais novidades",
            "preco": "R$ 00,00",
            "imagem": "fundo.jpg.png",
            "link_ml": "https://mercadolivre.com.br"
        },
        {
            "titulo": "Logo mais novidades",
            "preco": "R$ 00,00",
            "imagem": "fundo.jpg.png",
            "link_ml": "https://mercadolivre.com.br"
        },
        {
            "titulo": "Logo mais novidades",
            "preco": "R$ 00,00",
            "imagem": "fundo.jpg.png",
            "link_ml": "https://mercadolivre.com.br"
        },
        {
            "titulo": "Logo mais novidades",
            "preco": "R$ 00,00",
            "imagem": "fundo.jpg.png",
            "link_ml": "https://mercadolivre.com.br"
        },
        {
            "titulo": "Logo mais novidades",
            "preco": "R$ 00,00",
            "imagem": "fundo.jpg.png",
            "link_ml": "https://mercadolivre.com.br"
        },
        {
            "titulo": "Logo mais novidades",
            "preco": "R$ 00,00",
            "imagem": "fundo.jpg.png",
            "link_ml": "https://mercadolivre.com.br"
        }
        
    ]
    return render_template("produtos.html", anuncios=meus_anuncios)
