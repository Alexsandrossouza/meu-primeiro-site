@app.route("/jogos")
def jogos():
    # Lista de jogos fácil de atualizar!
    lista_de_jogos = [
        {
            "titulo": "Minecraft",
            "plataforma": "Xbox 360",
            "tamanho": "1.1 GB",
            "imagem": "Minecraft-Xbox-360-Edition.jpg",
            "link": "https://produto.mercadolivre.com.br/MLB-SEU-LINK-AQUI"
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