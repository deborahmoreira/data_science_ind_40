# Análise de dados para o PPCP: um estudo de caso

Dentre as principais atividades do setor de Planejamento, Programação e Controle da Produção está a geração de Ordens de Produção (OP). Estas determinam o início do fluxo produtivo de determinado produto e, como a companhia alvo do estudo de caso se trata de uma indústria têxtil, são eles calças, blusas, vestidos e demais artigos de vestuário. 
  Para que seja gerada uma OP, devem ser observadas algumas variáveis pertinentes. São elas:
* matéria-prima suficiente para suprir a necessidade;
* protótipo testado e aprovado pelo setor de engenharia;
* pedido emitido pelo setor de estilo e produto.

Em meio a uma enorme quantidade de dados gerados e consumidos no decorrer do processo fabril e com a agilidade requerida nesse âmbito, se faz necessário o uso de ferramentas que auxiliem o setor de PPCP a realizar uma de suas atividades-chave. As informações necessárias para executar a análise são organizadas naquele que é chamado de *Manufacturing Resources Planning* (MRP) e disponibilizadas em um arquivo de entrada em formato tabular. 

## Detalhando as transformações

O arquivo de entrada, contendo os dados de entrada, é lido e várias transformações são realizadas com objetivo de determinar quais produtos podem ou não ter sua OP gerada. Aqueles que não podem por possuir pêndencias relacionadas às variáveis citadas acima, devem ter essas especificadas, para que sejam posteriormente solucionadas. 

A figura abaixo ilustrar o passo a passo do que é realizado:

<center><img width="800" src="images/fluxo-de-dados.png"></center>

## Como executar

### Web
Para conhecer e navegar pelo projeto é recomendado acessar este [![Jupyter](https://img.shields.io/badge/-Notebook-191A1B?style=flat-square&logo=jupyter)](https://github.com/deborahmoreira/data_science_ind_40/blob/main/DataScience_PCP.ipynb)

Nele, a entrada é importada da nuvem, cada passo está organizado em seções, é possível visualisar textos explicativos e executar blocos de código individualmente. 
>Para executar todas as células de uma só vez use o comando `ctrl+F9`

>Para acessar os arquivos de saída, clique no menu à esquerda na aba "arquivos"

### Localmente

