# projeto-2up-grupo1
Projeto 2UP - Laboratório de Programação (UNIT-PE) - Grupo 1

# 🎬 CineRecife — Sistema de Gestão de Cinema

Projeto final da disciplina Laboratório de Programação 2026.2 — Profª Rafaella Matos

## Grupo 1

| Integrante | Matrícula | Usuário GitHub | Funções sob sua responsabilidade |
|---|---|---|---|

| Nicolas Diogenes Silva de Oliveira | 255313 | nicolasdiogenes | exibir_menu, buscar_filme, validar_idade, calcular_preco |

| Ana Gabriela Maria Mendes da Silva | 255259 | Anagmendes | ler_inteiro, cadastrar_filme, vender_ingresso, gerar_relatorio |

| Laura Luiza Rezende Bezerra | 255173 | lauurezende | listar_filmes, filmes_por_genero, cancelar_venda, menu principal e saída |

- Líder: Nicolas Diogenes
- Variante (pela matrícula do(a) líder): 2-3 — R$ 32,00, terça-feira, 25%, 50 assentos, Documentário

## Sobre o sistema
(Explique com suas palavras o que o sistema faz, em 3 a 5 linhas.)

## Como executar
1. Tenha o Python 3 instalado (ou use o Codespaces / Colab).
2. Baixe o arquivo `cinerecife.py`.
3. No terminal, rode: `python cinerecife.py`

## Funcionalidades
- [ ] Listar filmes
- [ ] Cadastrar filme
- [ ] Remover filme
- [ ] Buscar por gênero
- [ ] Vender ingresso
- [ ] Cancelar venda
- [ ] Relatório
(Marque com [x] o que funciona. Se algo ficou incompleto, explique aqui.)

## Estruturas de dados utilizadas
- Ana: No cadastro de filmes, utilizamos listas para armazenar os filmes, tuplas para guardar os horários das sessões, sets para controlar os assentos ocupados e dicionários para organizar os dados dos filmes. Na venda de ingressos, usamos listas e dicionários para registrar as vendas. Já no relatório, utilizamos sets para evitar gêneros repetidos e dicionários para contar os ingressos vendidos por filme.

## Como funciona cada parte

- Ana Gabriela: A função de ler inteiro serve para receber os números inteiros e verificar se eles estão no limite permitido. Usei while para repetir a mensagem até um número dentro do limite ser digitado e usei o try e o except para evitar erro caso o usuário digite um número que não pode ser convertido para inteiro. 
A função de cadastrar filmes serve para adicionar novos filmes ao sistema do CineRecife. Ela solicita as informações do filme, como código, título, gênero, classificação indicativa, duração e horários das sessões. Também verifica se os dados estão corretos e se o código já não está sendo utilizado. Depois, organiza essas informações em um dicionário e adiciona o filme à lista de filmes.
A função vender ingresso permite cadastrar os filmes que estarão disponíveis no sistema.
Já a função gerar relatório usa os registros das vendas para gerar os relatórios do cinema.
A função calcular_preco serve para calcular o valor final do ingresso. Ela considera o preço inteiro, aplica o desconto de 50% quando o ingresso é meia-entrada e, se for um dia promocional, aplica mais 30% de desconto sobre o valor já calculado.

Laura Rezende:

Nicolas Diogenes: A função de mostrar o menu, só imprime o menu com as opções.
A função de buscar o filme, o for percorre a lista e compara o código inserido com os códigos da lista, até encontrar o filme correspondente e retorna com as informações do filme. Os if verificam se o filme realmente existe ou é só um "None".
Por fim, a função de validade idade, compara a idade inserida com a classificação do filme, se ela for maior ou igual do que a classificação, sai True, se for menor, sai False. 

### Nome do integrante — funções: exemplo_1(), exemplo_2()
Ana Gabriela - funções: ler_inteiro(mensagem, minimo, maximo), cadastrar_filme(filmes), vender_ingresso(filmes, vendas, promocional) e gerar_relatorio(filmes, vendas) e calcular_preco(preco_base, tipo="inteira", promocional=False).

Laura Rezende - funções:

Nicolas Diogenes - funções: exibir_menu(), buscar_filme(filmes, codigo) e validar_idade(idade, classificacao)


## Exemplo de uso
(Cole aqui um trecho da saída do terminal de uma venda completa.)

## Maior dificuldade e como resolvi
- Ana: Minha maior dificuldade foi entender como organizar as informações e fazer as funções trabalharem juntas, principalmente no cadastro de filmes e na venda de ingressos. Consegui resolver pesquisando, estudando os comandos do Python e testando o código aos poucos, até entender como cada parte funcionava.

Laura: 

Nicolas: A minha maior dificuldade foi perceber que na funçao de validação de idade não precisa percorrer a lista, mas sim comparar a idade com a classificação do filme com o código do filme inserido, usando a função de buscar o filme (que é ela quem percorre a lista). Li o notion novamente, e no meio da leitura, eu percebi como que funcionava. 

## Declaração de uso de Inteligência Artificial
Marque UMA opção:

- [ X ] Declaro que NÃO utilizei nenhuma ferramenta de IA neste projeto.
- [ ] Declaro que utilizei IA apenas para os fins permitidos, conforme abaixo:

| Integrante | Ferramenta | Data | Pergunta feita (copie exatamente) | O que fez com a resposta |
|------------|------------|------|-----------------------------------|--------------------------|
|            |            |      |                                   |                          |

Declaramos que todo o código deste repositório foi escrito pelos integrantes do grupo.