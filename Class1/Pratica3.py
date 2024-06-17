# Conteúdo referente a Aula 1 de Lógica de Programação e Algoritmos
# Autor: Felipe Alafy Rodrigues Silva
# Criado em: 11/06/2024
# Última Modificação em: 11/06/2024
# Acesse o side Notes no meu Notion:
# https://www.notion.so/PA-L-gica-de-Programa-o-e-Algoritmos-b81c5cb3551e4a62b9b2c5b8b58fc2ac?pvs=4#d478ed82dd8d4c7683479d5ef03a7ef4

# Exercício 2
# Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo usuário,
# assim como a quantidade de dias pelos quais o carro foi alugado. Calcule o preço a pagar, sabendo que o carro custa
# R$ 60 por dia e R$ 0,15 por km rodado

km = float(input('Quantos Km o carro rodou? '))
dias_alugados = int(input('Por quantos dias você alugou o carro? '))

# Constantes são valores que nunca mudam, e portanto são escritas com letras maiusculas para diferenciar das variáveis
VALOR_DO_DIA_USADO = 60
VALOR_DO_KM_RODADO = 0.15

fatura_do_aluguel = (60 * VALOR_DO_DIA_USADO) + (VALOR_DO_KM_RODADO * 0.15)
print(f'O valor da fatura do aluguel do carro será de {fatura_do_aluguel}')
