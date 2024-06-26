# Exercício referente a Aula 3 de Lógica de Programação e Algoritmos
# Autor: Felipe Alafy Rodrigues Silva
# Criado em: 20/06/2024
# Última Modificação em: 20/06/2024
# Acesse o side Notes no meu Notion:
# https://www.notion.so/PA-L-gica-de-Programa-o-e-Algoritmos-b81c5cb3551e4a62b9b2c5b8b58fc2ac?pvs=4

# Exercício: Escreva um algoritmo em Python em que o usuário escolhe se quer comprar maçãs,  laranjas ou bananas.
# Deverá ser apresentado na tela um menu com as opções: 1 para maçã, 2 para laranja e 3 para banana.
# Após escolhida a fruta, deve-se digitar quantas unidades se quer comprar. O algoritmo deve calcular o preço total a
# pagar do produto escolhido e mostrá-lo na tela. Considere que uma maçã custa R$ 2,30, uma laranja, R$ 3,60,
# e uma banana, R$ 1,85

PRECO_MACA = 2.3
PRECO_LARANJA = 3.6
PRECO_BANANA = 1.85

print('-' * 80)
print("""Escolha a fruta que deseja comprar e digite o número correspondente:
Maçã - 1
Laranja - 2
Banana - 3""")

print('-' * 80)
codigo_fruta_selecionada = int(input('>> '))

if 1 < codigo_fruta_selecionada > 3:
    print('Não temos esse produto disponível no momento.')
    exit(0)

print('Digite a quantidade:')
quantidade = int(input('>> '))

if codigo_fruta_selecionada == 1:
    print(f'O preço total de {quantidade} maçãs fica em: {quantidade * PRECO_MACA}')
elif codigo_fruta_selecionada == 2:
    print(f'O preço total de {quantidade} laranjas fica em: {quantidade * PRECO_LARANJA}')
elif codigo_fruta_selecionada == 3:
    print(f'O preço total de {quantidade} bananas fica em: {quantidade * PRECO_BANANA}')

