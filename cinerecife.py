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