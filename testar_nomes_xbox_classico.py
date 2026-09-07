import os
import re
import sqlite3
import urllib.request

# ============================================================
# CONFIGURAÇÃO
# ============================================================

PASTA_CAPAS = os.path.join("static", "xbox classico")

BANCO = "MobCatsOGXboxTitleIDs.db"

URL_BANCO = "https://mobcat.zip/XboxIDs/titleIDs.db"

# ============================================================
# BAIXAR BANCO
# ============================================================

print("=" * 70)
print("TESTE DE IDENTIFICAÇÃO - XBOX CLÁSSICO")
print("=" * 70)
print()

if not os.path.exists(BANCO):

    print("Banco de dados não encontrado.")
    print("Baixando banco oficial do MobCat...")
    print()

    try:
        urllib.request.urlretrieve(URL_BANCO, BANCO)
        print("Banco baixado com sucesso!")

    except Exception as e:
        print("ERRO AO BAIXAR O BANCO:")
        print(e)
        input("\nPressione ENTER para sair...")
        raise SystemExit

else:
    print("Banco de dados já existe.")
    print()

# ============================================================
# ABRIR BANCO
# ============================================================

try:

    conexao = sqlite3.connect(BANCO)
    cursor = conexao.cursor()

    tabelas = cursor.execute(
        "SELECT name FROM sqlite_master WHERE type='table'"
    ).fetchall()

    print("Tabelas encontradas:")

    for tabela in tabelas:
        print(" -", tabela[0])

    print()

except Exception as e:

    print("ERRO AO ABRIR O BANCO:")
    print(e)

    input("\nPressione ENTER para sair...")
    raise SystemExit


# ============================================================
# DESCOBRIR COLUNAS
# ============================================================

mapa = {}

for tabela in tabelas:

    nome_tabela = tabela[0]

    try:

        colunas = cursor.execute(
            f'PRAGMA table_info("{nome_tabela}")'
        ).fetchall()

        nomes_colunas = [c[1] for c in colunas]

        print(f"Tabela: {nome_tabela}")
        print("Colunas:", nomes_colunas)
        print()

        # Procuramos uma tabela que tenha XMID
        # e algum campo de nome

        coluna_xmid = None
        coluna_nome = None

        for coluna in nomes_colunas:

            c = coluna.lower()

            if c == "xmid":
                coluna_xmid = coluna

            if c in (
                "full_name",
                "eng_name",
                "name",
                "title",
                "title_name"
            ):
                coluna_nome = coluna

        if coluna_xmid and coluna_nome:

            print("Tabela compatível encontrada!")
            print("XMID :", coluna_xmid)
            print("NOME :", coluna_nome)
            print()

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

            print(
                f"Jogos carregados desta tabela: {len(registros)}"
            )
            print()

    except Exception as e:

        print(
            f"Não foi possível analisar a tabela {nome_tabela}: {e}"
        )


# ============================================================
# VERIFICAR CAPAS
# ============================================================

if not os.path.isdir(PASTA_CAPAS):

    print("ERRO: pasta não encontrada:")
    print(PASTA_CAPAS)

    conexao.close()

    input("\nPressione ENTER para sair...")
    raise SystemExit


arquivos = [
    f for f in os.listdir(PASTA_CAPAS)
    if f.lower().endswith(
        (".jpg", ".jpeg", ".png", ".webp")
    )
]

print("=" * 70)
print("RESULTADO DO TESTE")
print("=" * 70)
print()

encontrados = 0
nao_encontrados = 0

for arquivo in sorted(arquivos):

    nome_sem_extensao = os.path.splitext(arquivo)[0]

    codigo = nome_sem_extensao.upper()

    # Primeiro tenta o código completo
    nome_jogo = mapa.get(codigo)

    # Se for uma variante PAL, tenta o código base
       # Primeiro tenta o código completo
    nome_jogo = mapa.get(codigo)

    # Se não encontrar, pega somente o XMID principal.
    # Exemplo:
    # VU00501K-NTSC-J-World-Collection
    # vira:
    # VU00501K

    if not nome_jogo:

        correspondencia = re.match(
            r"^([A-Z]{2}\d{5}[A-Z])",
            codigo
        )

        if correspondencia:

            codigo_base = correspondencia.group(1)

            nome_jogo = mapa.get(codigo_base)

    if nome_jogo:

        encontrados += 1

        print(f"[OK] {arquivo}")
        print(f"     -> {nome_jogo}")
        print()

    else:

        nao_encontrados += 1

        print(f"[??] {arquivo}")
        print("     -> Jogo não identificado")
        print()


# ============================================================
# RESUMO
# ============================================================

print("=" * 70)
print("RESUMO")
print("=" * 70)

print()
print(f"Capas encontradas:      {len(arquivos)}")
print(f"Identificadas:           {encontrados}")
print(f"Não identificadas:       {nao_encontrados}")

print()
print("NENHUM ARQUIVO FOI RENOMEADO.")
print("Este programa fez SOMENTE O TESTE.")

conexao.close()

input("\nPressione ENTER para sair...")