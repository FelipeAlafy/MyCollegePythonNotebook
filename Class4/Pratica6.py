# Conteúdo referente a Aula 4 de Lógica de Programação e Algoritmos Autor: Felipe Alafy Rodrigues Silva Criado em:
# 15/07/2024 Última Modificação em: 15/07/2024 Acesse o side Notes no meu Notion:
# https://www.notion.so/PA-L-gica-de-Programa-o-e-Algoritmos-b81c5cb3551e4a62b9b2c5b8b58fc2ac?pvs=4 Exercício 2
# Escreva um algoritmo que leia um valor e que imprima a quantidade de cédulas necessárias para pagar esse mesmo
# valor. Para simplificar, vamos trabalhar apenas com valores inteiros e com cédulas de R$ 100, R$ 50, R$ 20, R$ 10,
# R$ 5 e R$ 1


print('Notas disponiveis'.center(50, '-'))
print('R$ 100.00')
print('R$ 50.00')
print('R$ 20.00')
print('R$ 10.00')
print('R$ 5.00')
print('R$ 1.00')
valor = int(input('Digite o valor de saque desejado:'))
print('-' * 50)

notas100 = 0
notas50 = 0
notas20 = 0
notas10 = 0
notas5 = 0
notas1 = 0

while valor > 0:
    if valor >= 100:
        notas100 = valor // 100
        valor = valor - ((valor // 100) * 100)
    if valor >= 50:
        notas50 += valor // 50
        valor -= ((valor // 50) * 50)
    if valor >= 20:
        notas20 += valor // 20
        valor -= ((valor // 20) * 20)
    if valor >= 10:
        notas10 += valor // 10
        valor -= ((valor // 10) * 10)
    if valor >= 5:
        notas5 += valor // 5
        valor -= ((valor // 5) * 5)
    if valor >= 1:
        notas1 += valor // 1
        valor -= (valor // 1)

print('SAQUE'.center(50, '-'))
print(f'Notas de R$ 100.00: {notas100}')
print(f'Notas de R$ 50.00: {notas50}')
print(f'Notas de R$ 20.00: {notas20}')
print(f'Notas de R$ 10.00: {notas10}')
print(f'Notas de R$ 5.00: {notas5}')
print(f'Notas de R$ 1.00: {notas1}')
print('-' * 50)
