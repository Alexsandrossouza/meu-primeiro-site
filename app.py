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
            "titulo": "Console Playstation 5 Slim Edição Digital 825 Gb",
            "preco": "R$ 5.999",
            "imagem": "Console Playstation 5 Slim Edição Digital 825 Gb.webp",
            "link_ml": "https://www.mercadolivre.com.br/console-playstation-5-slim-edicao-digital-825-gb/p/MLB54963150?matt_event_ts=1784855563122&matt_d2id=f90b8b6f-d10a-46b9-8d34-121942b0a302&matt_tracing_id=9b062123-ff53-48b4-b067-68aee2c88129#polycard_client=recommendations_home_affiliate-profile&reco_backend=item_decorator&reco_client=home_affiliate-profile&matt_tool_id=64131546&reco_item_pos=0&source=affiliate-profile&reco_backend_type=function&reco_id=7355be09-2858-406d-8548-b2bea75a08ca&tracking_id=0e91f254-993b-4754-917a-4dd52d72b422&c_id=/home/card-featured/element&c_uid=e52090c4-6893-4538-a7e7-014145d6197e"
        },
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
            "titulo": "Console Sony Playstation 5 Edição Slim Disk 1tb Branco",
            "preco": "R$ 4.799",
            "imagem": "Console Sony Playstation 5 Edição Slim Disk 1tb Branco.webp",
            "link_ml": "https://www.mercadolivre.com.br/console-sony-playstation-5-edicao-slim-disk-1tb-branco-controle-sem-fio-dualsense-ps5-branco/p/MLB52897777?matt_event_ts=1784855828309&matt_d2id=f90b8b6f-d10a-46b9-8d34-121942b0a302&matt_tracing_id=063eb4df-e25d-4b19-b2dd-00706c6865ce#polycard_client=recommendations_home_affiliate-profile&reco_backend=item_decorator&reco_client=home_affiliate-profile&matt_tool_id=64131546&reco_item_pos=0&source=affiliate-profile&reco_backend_type=function&reco_id=cbe6155e-03a9-4679-aaab-7043d8c902c5&tracking_id=ef79fe72-937d-43a7-aae2-e3326b0bd274&c_id=/home/card-featured/element&c_uid=83431a9d-a1e6-4f68-8a58-95a3b01275d1"
        },
        {
            "titulo": "Controle Xbox Wireless",
            "preco": "R$ 449,00",
            "imagem": "Controle Xbox Wireless.webp",
            "link_ml": "https://www.mercadolivre.com.br/controle-xbox-wireless-series-xs-carbon-black/p/MLB16268160?matt_event_ts=1784854788466&matt_d2id=f90b8b6f-d10a-46b9-8d34-121942b0a302&matt_tracing_id=f378a9c6-f5db-4f85-9431-9179d9ca369c#polycard_client=recommendations_home_affiliate-profile&reco_backend=item_decorator&reco_client=home_affiliate-profile&matt_tool_id=64131546&reco_item_pos=0&source=affiliate-profile&reco_backend_type=function&reco_id=7227b8a6-476c-473c-ab96-cc9326b19a6e&tracking_id=d9d292f1-9185-4aa5-8b22-d3b7358331c3&c_id=/home/card-featured/element&c_uid=3ab3fc9c-94f0-4867-9c4e-9c917f03f5a8"
        },
        {
            "titulo": "Bateria Controle Para Xbox Séries S X 1200mah Cabo 3m",
            "preco": "R$ 58,99",
            "imagem": "Bateria Controle Para Xbox Séries S X 1200mah Cabo 3m.webp",
            "link_ml": "https://www.mercadolivre.com.br/bateria-controle-para-xbox-series-s-x-1200mah-cabo-3m/up/MLBU2183606506?pdp_filters=item_id%3AMLB5111737986&matt_event_ts=1784854708638&matt_d2id=f90b8b6f-d10a-46b9-8d34-121942b0a302&matt_tracing_id=bbaeb5d2-5e1d-4122-b944-2cb191b65be9#polycard_client=recommendations_home_affiliate-profile&wid=MLB5111737986&sid=recos&reco_backend=item_decorator&reco_client=home_affiliate-profile&matt_tool_id=64131546&reco_item_pos=0&source=affiliate-profile&reco_backend_type=function&reco_id=248e2154-2a69-4f9b-9e63-dd215d90d021&tracking_id=5114acaf-1fff-435d-a621-5e95f10f1a17&c_id=/home/card-featured/element&c_uid=9743aa93-d0d9-4daf-861a-6998a54d9ad3" 
        },
        {
            "titulo": "Adaptador Videogame Game Stick M15 2 Controles Game Stick",
            "preco": "R$ 189,90",
            "imagem": "Adaptador Videogame Game Stick M15 2 Controles Game Stick.webp",
            "link_ml": "https://www.mercadolivre.com.br/adaptador-videogame-game-stick-m15-2-controles-game-stick/up/MLBU3956288428?pdp_filters=item_id%3AMLB6737836486&matt_event_ts=1784854834364&matt_d2id=f90b8b6f-d10a-46b9-8d34-121942b0a302&matt_tracing_id=903a9199-9509-4c50-af51-82ab34adae9a#polycard_client=recommendations_home_affiliate-profile&wid=MLB6737836486&sid=recos&reco_backend=item_decorator&reco_client=home_affiliate-profile&matt_tool_id=64131546&reco_item_pos=0&source=affiliate-profile&reco_backend_type=function&reco_id=22e91bfa-e50d-49e2-b50a-3bdc053e8cfc&tracking_id=c28cb1f1-9c00-4e03-9450-8bdc3f43131e&c_id=/home/card-featured/element&c_uid=5d9c072e-5234-41a8-8983-c7675865d941"
        },
        {
            "titulo": "Pc Gamer Completo I7 3.4ghz 16gb Ssd 480gb 500w Monitor 19",
            "preco": "R$ 2026,58",
            "imagem": "Pc Gamer Completo I7 3.4ghz 16gb Ssd 480gb 500w Monitor 19.webp",
            "link_ml": "https://www.mercadolivre.com.br/pc-gamer-completo--i7-34ghz-16gb-ssd-480gb-500w-monitor-19/up/MLBU1986838950?pdp_filters=item_id%3AMLB4111977276&matt_event_ts=1784854876472&matt_d2id=f90b8b6f-d10a-46b9-8d34-121942b0a302&matt_tracing_id=8d33d786-f550-4b37-a787-7ea57ad1c830#polycard_client=recommendations_home_affiliate-profile&wid=MLB4111977276&sid=recos&reco_backend=item_decorator&reco_client=home_affiliate-profile&matt_tool_id=64131546&reco_item_pos=0&source=affiliate-profile&reco_backend_type=function&reco_id=a5fb4add-075b-46c9-a571-d527eb929e18&tracking_id=338d91f6-2912-4b4d-af64-2d7bec8721b2&c_id=/home/card-featured/element&c_uid=3e10b1ea-531b-46a9-b7ea-837595748f56"
        },
        {
            "titulo": "Smart TV 4K 50 LG Portal de Games Processador AI α7 Ger8 4K",
            "preco": "R$ 2.351,31",
            "imagem": "Smart TV 4K 50.webp",
            "link_ml": "https://www.mercadolivre.com.br/smart-tv-4k-50-lg-qned73-portal-de-games-processador-ai-7-ger8-4k-super-upscaling-google-cast-integrado-controle-ai-magic-webos-25-modo-esportes-alerta-de-esportes/p/MLB65916422?matt_event_ts=1784854921761&matt_d2id=f90b8b6f-d10a-46b9-8d34-121942b0a302&matt_tracing_id=13759d6b-ca39-4382-8ae8-bb0ad544ab0a#polycard_client=recommendations_home_affiliate-profile&reco_backend=item_decorator&reco_client=home_affiliate-profile&matt_tool_id=64131546&reco_item_pos=0&source=affiliate-profile&reco_backend_type=function&reco_id=0e7a4c83-caee-4b8c-b4bb-cfe7b43ac313&tracking_id=80a7a2c7-2411-4a7d-b05d-46105cf29aaa&c_id=/home/card-featured/element&c_uid=fd9ab8a8-6148-4b2a-83e0-20366381c17a"
        },
        {
            "titulo": "Bicicleta Elétrica Starmega V8 750W Preto",
            "preco": "R$ 5.930",
            "imagem": "Bicicleta Elétrica Starmega V8 750W Preto.webp",
            "link_ml": "https://www.mercadolivre.com.br/bicicleta-eletrica-starmega-v8-750w-preto-32kmh-bateria-48v-50km-autonomia/p/MLB62709217?matt_event_ts=1784852452281&matt_d2id=f90b8b6f-d10a-46b9-8d34-121942b0a302&matt_tracing_id=3bffc0b2-8743-401c-973f-e089abf38584#polycard_client=recommendations_home_affiliate-profile&reco_backend=item_decorator&reco_client=home_affiliate-profile&matt_tool_id=64131546&reco_item_pos=0&source=affiliate-profile&reco_backend_type=function&reco_id=e08982cd-74f0-4f0d-822f-df58384d2dc4&tracking_id=bfebed83-e8a2-4c67-b27d-12304a1ff151&c_id=/home/card-featured/element&c_uid=06724b41-cd72-430c-8500-eaf921b72d4a"
        },
        {
            "titulo": "Fonte Para Xbox 360 Slim Bivolt Conector 2 Pinos Com Cabo De Energia",
            "preco": "R$ 62,00",
            "imagem": "Fonte Para Xbox 360 Slim.webp",
            "link_ml": "https://www.mercadolivre.com.br/fonte-para-xbox-360-slim-bivolt-conector-2-pinos-com-cabo-de-energia-u-maisu/p/MLB68824482?matt_event_ts=1784855371221&matt_d2id=f90b8b6f-d10a-46b9-8d34-121942b0a302&matt_tracing_id=bc9b8d58-7167-45fe-92c0-2d58299a47f6#polycard_client=recommendations_home_affiliate-profile&reco_backend=item_decorator&reco_client=home_affiliate-profile&matt_tool_id=64131546&reco_item_pos=0&source=affiliate-profile&reco_backend_type=function&reco_id=09ae3e1d-fc7c-4df2-a245-402526c490f5&tracking_id=b41e3428-1dc0-479b-aa2e-ea5fe448d6b0&c_id=/home/card-featured/element&c_uid=b53849f6-547f-43df-957f-29de2303d02f"
        },
        {
            "titulo": "Console Sony Playstation 5 Edição Slim Disk 1tb Branco",
            "preco": "R$ 4.799",
            "imagem": "Console Sony Playstation 5 Edição Slim Disk 1tb Branco.webp",
            "link_ml": "https://www.mercadolivre.com.br/console-sony-playstation-5-edicao-slim-disk-1tb-branco-controle-sem-fio-dualsense-ps5-branco/p/MLB52897777?matt_event_ts=1784855828309&matt_d2id=f90b8b6f-d10a-46b9-8d34-121942b0a302&matt_tracing_id=063eb4df-e25d-4b19-b2dd-00706c6865ce#polycard_client=recommendations_home_affiliate-profile&reco_backend=item_decorator&reco_client=home_affiliate-profile&matt_tool_id=64131546&reco_item_pos=0&source=affiliate-profile&reco_backend_type=function&reco_id=cbe6155e-03a9-4679-aaab-7043d8c902c5&tracking_id=ef79fe72-937d-43a7-aae2-e3326b0bd274&c_id=/home/card-featured/element&c_uid=83431a9d-a1e6-4f68-8a58-95a3b01275d1"
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
