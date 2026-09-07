import os
import re
import csv
import sqlite3

# ============================================================
# CONFIGURAÇÃO
# ============================================================

PASTA_CAPAS = os.path.join("static", "xbox classico")

BANCO = "MobCatsOGXboxTitleIDs.db"

ARQUIVO_LOG = "renomeacao_xbox_classico.csv"

# ============================================================
# FUNÇÃO PARA LIMPAR NOMES
# ============================================================

def limpar_nome(nome):
    """
    Remove caracteres que não podem fazer parte
    de um nome de arquivo.
    """

    nome = str(nome).strip()

    nome = re.sub(r'[<>:"/\\|?*]', '', nome)

    nome = re.sub(r'\s+', ' ', nome)

    nome = nome.strip(" .")

    return nome


# ============================================================
# FUNÇÃO PARA EVITAR ARQUIVO DUPLICADO
# ============================================================

def nome_disponivel(caminho):

    if not os.path.exists(caminho):
        return caminho

    pasta = os.path.dirname(caminho)

    nome = os.path.basename(caminho)

    base, extensao = os.path.splitext(nome)

    contador = 2

    while True:

        novo_nome = f"{base} ({contador}){extensao}"

        novo_caminho = os.path.join(
            pasta,
            novo_nome
        )

        if not os.path.exists(novo_caminho):
            return novo_caminho

        contador += 1


# ============================================================
# VERIFICAR PASTA
# ============================================================

if not os.path.isdir(PASTA_CAPAS):

    print()
    print("ERRO: a pasta não foi encontrada:")
    print(PASTA_CAPAS)

    input("\nPressione ENTER para sair...")
    raise SystemExit


# ============================================================
# VERIFICAR BANCO
# ============================================================

if not os.path.exists(BANCO):

    print()
    print("ERRO: banco de dados não encontrado:")
    print(BANCO)

    print()
    print("Execute primeiro:")
    print("python testar_nomes_xbox_classico.py")

    input("\nPressione ENTER para sair...")
    raise SystemExit


# ============================================================
# ABRIR BANCO
# ============================================================

print("=" * 70)
print("RENOMEADOR DE CAPAS - XBOX CLÁSSICO")
print("=" * 70)
print()

print("Abrindo banco de dados...")

try:

    conexao = sqlite3.connect(BANCO)

    cursor = conexao.cursor()

except Exception as e:

    print("ERRO AO abrir o banco:")
    print(e)

    input("\nPressione ENTER para sair...")
    raise SystemExit


# ============================================================
# CRIAR MAPA XMID -> NOME
# ============================================================

mapa = {}

tabelas = cursor.execute(
    "SELECT name FROM sqlite_master WHERE type='table'"
).fetchall()


for tabela in tabelas:

    nome_tabela = tabela[0]

    try:

        colunas = cursor.execute(
            f'PRAGMA table_info("{nome_tabela}")'
        ).fetchall()

        nomes_colunas = [c[1] for c in colunas]

        coluna_xmid = None
        coluna_nome = None

        for coluna in nomes_colunas:

            coluna_lower = coluna.lower()

            if coluna_lower == "xmid":
                coluna_xmid = coluna

            if coluna_lower in (
                "full_name",
                "eng_name",
                "name",
                "title",
                "title_name"
            ):
                coluna_nome = coluna

        if coluna_xmid and coluna_nome:

            registros = cursor.execute(
                f'''
                SELECT "{coluna_xmid}", "{coluna_nome}"
                FROM "{nome_tabela}"
                WHERE "{coluna_xmid}" IS NOT NULL
                '''
            ).fetchall()

            for xmid, nome in registros:

                if xmid and nome:

                    mapa[str(xmid).upper()] = str(nome).strip()

    except Exception:

        pass


print(
    f"Jogos encontrados no banco: {len(mapa)}"
)

print()


# ============================================================
# PEGAR CAPAS
# ============================================================

arquivos = [
    f
    for f in os.listdir(PASTA_CAPAS)
    if f.lower().endswith(
        (".jpg", ".jpeg", ".png", ".webp")
    )
]

print(
    f"Capas encontradas na pasta: {len(arquivos)}"
)

print()


# ============================================================
# CONFIRMAÇÃO
# ============================================================

print("=" * 70)
print("ATENÇÃO")
print("=" * 70)

print()
print("O programa vai renomear somente as capas")
print("que forem identificadas pelo banco.")
print()
print("As capas não identificadas permanecerão exatamente")
print("com os nomes atuais.")
print()
print("Nenhuma capa será apagada.")
print()

resposta = input(
    "Digite RENOMEAR para continuar: "
).strip().upper()

if resposta != "RENOMEAR":

    print()
    print("Operação cancelada.")
    print("Nenhum arquivo foi alterado.")

    conexao.close()

    input("\nPressione ENTER para sair...")
    raise SystemExit


# ============================================================
# RENOMEAR
# ============================================================

renomeadas = 0
nao_identificadas = 0
erros = 0

log = []


for arquivo in sorted(arquivos):

    nome_sem_extensao, extensao = os.path.splitext(
        arquivo
    )

    codigo = nome_sem_extensao.upper()

    # --------------------------------------------------------
    # TENTAR CÓDIGO COMPLETO
    # --------------------------------------------------------

    nome_jogo = mapa.get(codigo)

    # --------------------------------------------------------
    # PEGAR XMID PRINCIPAL
    #
    # Exemplo:
    #
    # VU00501K-NTSC-J-World-Collection
    #
    # vira:
    #
    # VU00501K
    # --------------------------------------------------------

    codigo_principal = None

    if not nome_jogo:

        correspondencia = re.match(
            r"^([A-Z]{2}\d{5}[A-Z])",
            codigo
        )

        if correspondencia:

            codigo_principal = correspondencia.group(1)

            nome_jogo = mapa.get(codigo_principal)

    else:

        codigo_principal = codigo


    # --------------------------------------------------------
    # NÃO IDENTIFICADO
    # --------------------------------------------------------

    if not nome_jogo:

        nao_identificadas += 1

        log.append([
            arquivo,
            "",
            "NAO IDENTIFICADO"
        ])

        continue


    # --------------------------------------------------------
    # LIMPAR NOME DO JOGO
    # --------------------------------------------------------

    nome_jogo = limpar_nome(nome_jogo)


    # --------------------------------------------------------
    # PRESERVAR INFORMAÇÕES DA CAPA
    #
    # Exemplo:
    #
    # VU00501K-NTSC-J-World-Collection.jpg
    #
    # vira:
    #
    # Buffy - Chaos Bleeds - NTSC-J - World-Collection.jpg
    # --------------------------------------------------------

    informacao_extra = ""

    if codigo_principal:

        resto = codigo[
            len(codigo_principal):
        ]

        if resto:

            resto = resto.lstrip("-_ ")

            if resto:

                partes = re.split(
                    r"[-_]+",
                    resto
                )

                partes = [
                    p.strip()
                    for p in partes
                    if p.strip()
                ]

                if partes:

                    informacao_extra = " - ".join(
                        partes
                    )


    # --------------------------------------------------------
    # MONTAR NOVO NOME
    # --------------------------------------------------------

    if informacao_extra:

        novo_nome = (
            f"{nome_jogo} - "
            f"{informacao_extra}"
            f"{extensao.lower()}"
        )

    else:

        novo_nome = (
            f"{nome_jogo}"
            f"{extensao.lower()}"
        )


    novo_nome = limpar_nome(novo_nome)


    # --------------------------------------------------------
    # CAMINHO ANTIGO E NOVO
    # --------------------------------------------------------

    caminho_antigo = os.path.join(
        PASTA_CAPAS,
        arquivo
    )

    caminho_novo = os.path.join(
        PASTA_CAPAS,
        novo_nome
    )


    # --------------------------------------------------------
    # SE FOR O MESMO NOME
    # --------------------------------------------------------

    if os.path.abspath(caminho_antigo) == os.path.abspath(caminho_novo):

        continue


    # --------------------------------------------------------
    # EVITAR SOBRESCREVER
    # --------------------------------------------------------

    caminho_novo = nome_disponivel(
        caminho_novo
    )

    novo_nome_final = os.path.basename(
        caminho_novo
    )


    # --------------------------------------------------------
    # RENOMEAR
    # --------------------------------------------------------

    try:

        os.rename(
            caminho_antigo,
            caminho_novo
        )

        renomeadas += 1

        log.append([
            arquivo,
            novo_nome_final,
            "RENOMEADO"
        ])

        print(
            f"[OK] {arquivo}"
        )

        print(
            f"     -> {novo_nome_final}"
        )

    except Exception as e:

        erros += 1

        log.append([
            arquivo,
            novo_nome_final,
            f"ERRO: {e}"
        ])

        print(
            f"[ERRO] {arquivo}"
        )

        print(
            f"       {e}"
        )


# ============================================================
# SALVAR LOG
# ============================================================

try:

    with open(
        ARQUIVO_LOG,
        "w",
        newline="",
        encoding="utf-8-sig"
    ) as arquivo_csv:

        escritor = csv.writer(
            arquivo_csv
        )

        escritor.writerow([
            "Nome antigo",
            "Nome novo",
            "Status"
        ])

        escritor.writerows(log)

except Exception as e:

    print()
    print(
        "AVISO: não foi possível salvar o arquivo de log:"
    )

    print(e)


# ============================================================
# FECHAR BANCO
# ============================================================

conexao.close()


# ============================================================
# RESUMO
# ============================================================

print()
print("=" * 70)
print("RENOMEAÇÃO CONCLUÍDA")
print("=" * 70)

print()
print(
    f"Capas encontradas:       {len(arquivos)}"
)

print(
    f"Capas renomeadas:        {renomeadas}"
)

print(
    f"Não identificadas:       {nao_identificadas}"
)

print(
    f"Erros:                   {erros}"
)

print()
print(
    f"Log salvo em: {ARQUIVO_LOG}"
)

print()
print("Nenhuma capa foi apagada.")

input("\nPressione ENTER para sair...")