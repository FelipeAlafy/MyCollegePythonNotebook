# Exercício referente a Aula 3 de Lógica de Programação e Algoritmos
# Autor: Felipe Alafy Rodrigues Silva
# Criado em: 04/07/2024
# Última Modificação em: 20/06/2024
# Acesse o side Notes no meu Notion:
# https://www.notion.so/PA-L-gica-de-Programa-o-e-Algoritmos-b81c5cb3551e4a62b9b2c5b8b58fc2ac?pvs=4

# Exercício 2
# Escreva um algoritmo que leia dois valores numéricos e que pergunte ao usuário qual operação ele deseja
# realizar: adição (+), subtração (-), multiplicação (*) ou divisão (/). Exiba na tela o resultado da operação
# desejada (exercício da apostila — aula 3)

valor1 = float(input('Por favor, digite o primeiro valor: '))
valor2 = float(input('Por favor, digite o segundo valor: '))
op = int(input('1 = Soma\n2 = Subtração\n3 = multiplicação\n4 = divisão\nPor favor selecione a operação:'))

resultado = 0.0
if op == 4 and valor2 == 0:
    print('Operação impossível detectada, fechando a calculadora.')
    exit(0)

if op == 1:
    resultado = valor1 + valor2
elif op == 2:
    resultado = abs(valor1 - valor2)
elif op == 3:
    resultado = valor1 * valor2
elif op == 4:
    resultado = valor1 / valor2
else:
    print('Operação inexistente, fechando calculadora.')
print(f'O resultado é {resultado}')
