from flask import Flask, render_template

app = Flask(__name__)

# ROTA DA PÁGINA INICIAL
@app.route("/")
def index():
    return render_template("index.html")

# ROTA DA PÁGINA DE JOGOS
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
            "imagem": "Resident-Evil-Operation-Raccoon-City.jpg",
            "link": "https://produto.mercadolivre.com.br/MLB-SEU-LINK-AQUI"
        }
        
        # Para adicionar um jogo novo, é só copiar e colar um bloco desse aqui!
    ]
    return render_template("jogos.html", jogos=lista_de_jogos)