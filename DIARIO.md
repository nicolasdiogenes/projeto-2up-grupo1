# Diário de desenvolvimento — CineRecife

## 26/11 — 9h30 — Nicolas Diogenes
- O que fiz: montei a base do código, separei com o resto do grupo as funções em que cada um será responsável e iníciei a função de mostrar o menu. 
- Erro ou dificuldade: nenhuma 
- Como resolvi: -- -- 
- Próximo passo: organizar o repositório.

## 26/11 — 21h50 — Nicolas Diogenes
- O que fiz: enviei os convites de colaboradores. 
- Erro ou dificuldade: nenhum 
- Como resolvi: 
- Próximo passo: clonar o repositório no vscode.

## 27/11 — 20h40 — Nicolas Diogenes
- O que fiz: adicionei o arquivo do diário (tinha esquecido rs), comecei a testar a função de mostrar o menu e criei a função de buscar_filme(filmes,codigo)
- Erro ou dificuldade: percorrer a lista de dicionários 
- Como resolvi: eu tinha esquecido de criar a varável "filme" que guarda o item da lista
- Próximo passo: criar função validar_idade(idade, classificacao).

## 28/11 - 10:27 - Ana Gabriela
- O que fiz: clonei o repositório na minha máquina e dei git pull para poder iniciar minhas alterações.
- próximo passo: organizar e criar minhas funções.

## 28/11 - 12:05 - Ana Gabriela
- O que fiz: Criei a função ler_inteiro(mensagem, minimo, maximo), responsável por receber números inteiros dentro de um intervalo definido. Também desenvolvi as funções cadastrar_filme(filmes), para cadastrar filmes e suas sessões; vender_ingresso(filmes, vendas, promocional), para realizar as vendas e verificar a disponibilidade dos assentos; e gerar_relatorio(filmes, vendas), para apresentar os resultados das vendas e outras informações do cinema.
- Erro ou dificuldade: Tive dificuldade em montar os laços de repetição, organizar as informações nos dicionários e fazer todas as verificações necessárias durante o cadastro e a venda de ingressos. Também tive dificuldade em organizar os cálculos do relatório.. 
- Como resolvi: Percebi que havia esquecido de utilizar o try para tratar entradas inválidas que não poderiam ser convertidas em números inteiros. Para as outras funções, organizei o código por etapas, utilizei condições e laços de repetição e testei cada parte para entender melhor seu funcionamento e corrigir os erros encontrados.

## 28/11 - 12:14 - Ana Gabriela
- O que fiz: Escolhi fazer a função calcular_preco também, para calcular o valor final dos ingressos, considerando o tipo de ingresso (inteira ou meia-entrada) e o desconto aplicado em dias promocionais.
- Erro ou dificuldade: Tive dificuldade porque a função estava sendo chamada na venda de ingressos, mas ainda não havia sido criada.
- Como resolvi: Criei a função separadamente, utilizando condições if para verificar o tipo de ingresso e se o dia era promocional. Depois, retornei o valor final para ser utilizado na função de venda.


## 28/11 — 12h40 — Nicolas Diogenes
- O que fiz: criei e testei a função validar_idade(idade,filme). 
- Erro ou dificuldade: de alguma forma, achei que funcionava da mesma forma que a função de buscar filmes e comcei usando um for pra percorrer, mas não era assim. 
- Como resolvi: vi que dava uns erros e reli o notion, daí que eu percebi que a função usava apenas um if pra comparar, sem percorrer a lista. 