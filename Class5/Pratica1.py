# Conteúdo referente a Aula 5 de Lógica de Programação e Algoritmos
# Autor: Felipe Alafy Rodrigues Silva
# Criado em: 07/07/2024
# Última Modificação em: 07/07/2024
# Acesse o side Notes no meu Notion:
# https://www.notion.so/PA-L-gica-de-Programa-o-e-Algoritmos-b81c5cb3551e4a62b9b2c5b8b58fc2ac?pvs=4

# Exercício 1
# Escreva uma rotina que crie uma borda ao redor de uma palavra, para destacá-la como sendo um
# título. A rotina deve receber como parâmetro a palavra a ser destacada. O tamanho da caixa de
# texto deverá ser adaptável, de acordo com o tamanho da palavra.

def borda(palavra):
    len_palavra = len(palavra)
    print(f'+{"-" * len_palavra}+')
    print(f'|{palavra}|')
    print(f'+{"-" * len_palavra}+')


borda('Felipe Alafy Rodrigues Silva')
borda('Vinicius')
borda('Aula 5')
