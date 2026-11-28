PRECO_INTEIRA = 32.00          # valor da sua variante
CAPACIDADE = 50                # valor da sua variante
CLASSIFICACOES_VALIDAS = (0, 10, 12, 14, 16, 18)   # 0 = Livre

filmes = [
    {"codigo": 101, "titulo": "Maré Alta no Capibaribe", "genero": "Drama",
     "classificacao": 12, "duracao": 110, "sessoes": ("14:00", "19:00"),
     "ocupados": {"14:00": set(), "19:00": set()}},
    {"codigo": 102, "titulo": "Robôs do Sertão", "genero": "Ficção científica",
     "classificacao": 10, "duracao": 95, "sessoes": ("15:30", "18:00", "20:30"),
     "ocupados": {"15:30": set(), "18:00": set(), "20:30": set()}},
    {"codigo": 103, "titulo": "O Segredo do Casarão", "genero": "Terror",
     "classificacao": 16, "duracao": 102, "sessoes": ("21:00",),
     "ocupados": {"21:00": set()}},
    {"codigo": 104, "titulo": "Frevo no Pé", "genero": "Comédia",
     "classificacao": 0, "duracao": 88, "sessoes": ("13:00", "16:00"),
     "ocupados": {"13:00": set(), "16:00": set()}},
     {"codigo": 105, "titulo": "O dilema dos apps", "genero": "Documentário", 
      "classificacao": 12, "duracao": 97, "sessoes": ("13:00", "15:30"),
      "ocupados": {"13:00": set(), "15:30": set()}},
]

vendas = []   # cada venda será um dictionary


#Responsável: Nicolas Diogenes
def exibir_menu():
    print("===== CINERECIFE =====\n 1 - Listar filmes em cartaz\n 2 - Cadastrar filme\n 3 - Remover filme \n 4 - Buscar filmes por gênero\n 5 - Vender ingresso\n 6 - Cancelar venda \n 7 - Relatório da bilheteria\n 0 - Sair")

#Responsável: Nicolas Diogenes
def buscar_filme(filmes, codigo):
    for filme in filmes:
        if filme["codigo"] == codigo:
            return filme
    return None

exibir_menu()


# Gente, quando forem usar a função de buscar, coloquem esse bloco aqui
codcomp = int(input("Digite o código do filme: "))
resultado = buscar_filme(filmes, codcomp)

if resultado is None:
    print("Filme não encontrado.")
else:
    print(resultado["titulo"])

#até aqui

#Responsável: Ana Gabriela 
def ler_inteiro(mensagem, minimo, maximo):
    while True:
        try:
            numero = int(input(mensagem))

            if minimo <= numero <= maximo:
                return numero
            else:
                print(f"Digite um número entre {minimo} e {maximo}.")
        except ValueError:
            print("Entrada Inválida! Digite um número inteiro.")

#Reponsável: Ana Gabriela
def cadastrar_filmes(filmes):
    print("\n===== CADASTRAR FILME =====")

    while True:
        codigo = ler_inteiro("Código do filme: ", 1, 999999)

        if buscar_filme(filmes, codigo) is None:
            break
        print("Esse código já está cadastrado.  ")

    while True:
        titulo = input("Título do filme: ").strip()

        if titulo:
            break
        print("O título não pode ficar vazio.")

    genero = input("Gênero do filme: ").strip()

    print("Classificações disponíveis: ", CLASSIFICACOES_VALIDAS)

    while True:
        classificacao = ler_inteiro("Classificação indicativa: ", 0, 18)

        if classificacao in CLASSIFICACOES_VALIDAS:
            break
        print("Classificação inválida.")

    duracao = ler_inteiro(  "Duração em minutos: ", 60, 240)

    quantidade = ler_inteiro("Quantas sessões terá o filme (1 a 4)? ", 1, 4)

    sessoes_lista = []

    for i in range(quantidade):
        horario = input(f"Horário da sessão {i+1}:").strip()

        sessoes_lista.append(horario)

    sessoes = tuple(sessoes_lista)

    ocupados = {}

    for horario in sessoes:
        ocupados[horario] = set()

    novo_filme = {
        "codigo": codigo,
        "titulo": titulo,
        "genero": genero,
        "classificacao": classificacao,
        "duracao": duracao,
        "sessoes": sessoes,
        "ocupados": ocupados
    }

    filmes.append(novo_filme)

    print("\nFilme cadastrado com sucesso!")


#Responsável: Ana Gabriela

def vender_ingressos(filmes, vendas, promocional):
    print("\n===== VENDA DE INGRESSO =====")

    codigo = ler_inteiro("Código do filme: ", 1, 999999)

    filme = buscar_filme(filmes, codigo)

    if filme is None:
        print("Filme não encontrado.")
        return
    
    print("\nSessões disponíveis:")

    for i, horario in enumerate(filme["sessoes"], start=1):
        print(f"{i} - {horario}")

    escolha = ler_inteiro(
        "Escolha a sessão: ", 1, len(filme["sessoes"])
    )

    sessao = filme["sessoes"][escolha - 1]

    ocupados = filme["ocupados"][sessao]

    if len(ocupados) >= CAPACIDADE:
        print("Sessão lotada.")
        return

    idade = ler_inteiro("Idade do cliente: ", 0, 120)

    if idade < filme["classificacao"]:
        print(
            f"Venda bloqueada: filme para maiores de "
            f"{filme['classificacao']} anos"
        )
        return

    while True:
        preferencial = input(
            "Cliente preferencial? (S/N): "
        ).strip().upper()

        if preferencial in ("S", "N"):
            break

        print("Digite S ou N.")

    assentos_livres = [
        assento
        for assento in range(1, CAPACIDADE + 1)
        if assento not in ocupados
    ]

    print("\nAssentos livres:")
    print(assentos_livres)

    while True:
        assento = ler_inteiro(
            "Número do assento: ", 1, CAPACIDADE
        )

        if assento in ocupados:
            print("Esse assento já está ocupado.")
            continue

        if assento <= 5 and preferencial == "N":
            print(
                "Assentos de 1 a 5 são reservados "
                "para clientes preferenciais."
            )
            continue

        break

    while True:
        tipo = input(
            "Tipo de ingresso (I - Inteira / M - Meia): "
        ).strip().upper()

        if tipo in ("I", "M"):
            break

        print("Opção inválida.")

    if tipo == "M":
        tipo_ingresso = "meia"
    else:
        tipo_ingresso = "inteira"

    valor = calcular_preco(
        PRECO_INTEIRA,
        tipo=tipo_ingresso,
        promocional=promocional
    )

    ocupados.add(assento)

    venda = {
        "id": len(vendas) + 1,
        "codigo_filme": filme["codigo"],
        "titulo": filme["titulo"],
        "sessao": sessao,
        "assento": assento,
        "tipo": tipo_ingresso,
        "valor": valor
    }

    vendas.append(venda)

    print("\n===== COMPROVANTE DE VENDA =====")
    print("ID:", venda["id"])
    print("Código do filme:", venda["codigo_filme"])
    print("Filme:", venda["titulo"])
    print("Sessão:", venda["sessao"])
    print("Assento:", venda["assento"])
    print("Tipo:", venda["tipo"].capitalize())
    print(f"Valor: R$ {venda['valor']:.2f}")
    print("================================")

#Responsável: Ana Gabriela

def gerar_relatorio(filmes, vendas):
    print("\n===== RELATÓRIO DA BILHETERIA =====")

    total_arrecadado = sum(
        venda["valor"] for venda in vendas
    )

    inteiras = sum(
        1 for venda in vendas
        if venda["tipo"] == "inteira"
    )

    meias = sum(
        1 for venda in vendas
        if venda["tipo"] == "meia"
    )

    print("\n--- Arrecadação ---")
    print("Ingressos vendidos:", len(vendas))
    print("Ingressos inteiros:", inteiras)
    print("Meias-entradas:", meias)
    print(f"Total arrecadado: R$ {total_arrecadado:.2f}")

    if not vendas:
        print("\nAinda não existem vendas registradas.")

    contagem_filmes = {}

    for filme in filmes:
        contagem_filmes[filme["titulo"]] = 0

    for venda in vendas:
        titulo = venda["titulo"]
        contagem_filmes[titulo] += 1

    print("\n--- Ingressos por filme ---")

    for titulo, quantidade in contagem_filmes.items():
        print(f"{titulo}: {quantidade} ingresso(s)")

    if vendas:
        mais_vendido = max(
            contagem_filmes,
            key=contagem_filmes.get
        )

        print("\nFilme com mais ingressos vendidos:")
        print(mais_vendido)
        print(
            "Quantidade:",
            contagem_filmes[mais_vendido]
        )

    print("\n--- Taxa de ocupação ---")

    for filme in filmes:
        print(f"\nFilme: {filme['titulo']}")

        for sessao in filme["sessoes"]:
            ocupados = len(filme["ocupados"][sessao])

            taxa = (ocupados / CAPACIDADE) * 100

            print(
                f"Sessão {sessao}: "
                f"{ocupados}/{CAPACIDADE} lugares "
                f"({taxa:.2f}%)"
            )

    generos = set()

    for filme in filmes:
        generos.add(filme["genero"])

    generos_ordenados = sorted(generos)

    print("\n--- Gêneros em cartaz ---")

    for genero in generos_ordenados:
        print(genero)

    print("\n--- Simulação de reajuste de 10% ---")

    valores_reajustados = list(
        map(
            lambda venda: venda["valor"] * 1.10,
            vendas
        )
    )

    if valores_reajustados:
        for i, valor in enumerate(valores_reajustados, start=1):
            print(f"Venda {i}: R$ {valor:.2f}")
    else:
        print("Não existem vendas para simular o reajuste.")

    print("\n===================================")