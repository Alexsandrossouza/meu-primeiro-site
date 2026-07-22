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
            "titulo": "Minecraft",
            "plataforma": "Xbox 360",
            "tamanho": "1.460 GB",
            "imagem": "Minecraft-Xbox-360-Edition.jpg",
            "link": "https://sto1.romsforever.co/0:/Xbox-360-Digital/Minecraft%20-%20Xbox%20360%20Edition%20(World)%20(v61)%20(Title%20Update).zip?token=c3xZcFthXAVOQyAgUX5VMw4ATkUlcFl%2BVmZQAk4VdXMNfgBmCQAIEHZ8XXFYZFFRRg%3D%3D"
        },
        {
            "titulo": "Resident Evil Operation Raccoon City",
            "plataforma": "Xbox 360",
            "tamanho": "4.2 GB",
            "imagem": "Resident-Evil-Operation-Raccoon-City-Special-Edition.jpg",
            "link": "https://produto.mercadolivre.com.br/MLB-SEU-LINK-AQUI"
        },
        {
            "titulo": "Grand Theft Auto V",
            "plataforma": "Xbox 360",
            "tamanho": "16.5 GB",
            "imagem": "Grand-Theft-Auto-V.jpg",
            "link": "https://produto.mercadolivre.com.br/MLB-LINK-GTA"
        },
        {
            "titulo": "Gears of War 3",
            "plataforma": "Xbox 360",
            "tamanho": "7.5 GB",
            "imagem": "Gears-of-War-3-scaled.jpg",
            "link": "https://produto.mercadolivre.com.br/MLB-LINK-GEARS"
        },
        {
            "titulo": "Assassin's creed rogue",
            "plataforma": "Xbox 360",
            "tamanho": "5.5 GB",
            "imagem": "Assassin's creed rogue.jpg",
            "link": "https://www.mediafire.com/file/willx6ys2qozko8/uGA&ugTkvX6a.rar/file"
        },
        {
            "titulo": "Red Dead Redemption",
            "plataforma": "Xbox 360",
            "tamanho": "7.5 GB",
            "imagem": "red-dead-redemption-game-of-the-year-edition-xbox-360-1_orig.jpg",
            "link_part1": "https://www.mediafire.com/file/6adboemuos4q8tu/lRIdF9u$UZh.part1.rar/file",
            "link_part2": "https://www.mediafire.com/file/1dh6q2hfdtqb2t3/lrIdF9u$UZh.part2.rar/file"
        },
        {
            "titulo": "Grand Theft Auto V",
            "plataforma": "Xbox 360",
            "tamanho": "16.5 GB",
            "imagem": "gta-v.jpg",
            "link": "https://produto.mercadolivre.com.br/MLB-LINK-GTA"
        },
        {
            "titulo": "Gears of War 3",
            "plataforma": "Xbox 360",
            "tamanho": "7.5 GB",
            "imagem": "gears-of-war-3.jpg",
            "link": "https://produto.mercadolivre.com.br/MLB-LINK-GEARS"
        },
        {
            "titulo": "skyrim",
            "plataforma": "Xbox 360",
            "tamanho": "4.36 GB",
            "imagem": "skyrim.jpg",
            "link": "https://www.mediafire.com/file/iguca3f8nfnb71y/6%2525NBmVHwdPY%2526.rar/file"
        },
        {
            "titulo": "Assassin's Creed Rogue",
            "plataforma": "Xbox 360",
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
            "preco": "R$ 1450,00",
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
            "titulo": "Logo mais novidades",
            "preco": "R$ 0,00",
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
