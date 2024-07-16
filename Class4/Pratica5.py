# Conteúdo referente a Aula 4 de Lógica de Programação e Algoritmos
# Autor: Felipe Alafy Rodrigues Silva
# Criado em: 15/07/2024
# Última Modificação em: 15/07/2024
# Acesse o side Notes no meu Notion:
# https://www.notion.so/PA-L-gica-de-Programa-o-e-Algoritmos-b81c5cb3551e4a62b9b2c5b8b58fc2ac?pvs=4

# Exercício 1
# Escreva um algoritmo que mostra, na tela, quatro produtos a serem comprados em uma lanchonete:
# • Coxinha - R$ 5,00
# • Pastel - R$ 7,00
# • Café - R$ 4,00
# • suco - R$ 6,00
# Faça um algoritmo em que você seleciona o produto que quer comprar e a quantidade. Faça isso até que decida
# encerrar o programa. Ao final, mostre o valor final do pedido a ser pago

valor_final = 0

while True:
    print('menu'.center(50, '-'))
    print('1 - Coxinha - R$ 5.00')
    print('2 - Pastel - R$ 7.00')
    print('3 - Café - R$ 4.00')
    print('4 - Suco - R$ 6.00')
    print('0 - Encerrar compra')
    op = int(input('Digite a opção desejada: '))
    print('-' * 50)
    if op > 4 or op < 0:
        continue
    if op == 1:
        valor_final += 5
    elif op == 2:
        valor_final += 7
    elif op == 3:
        valor_final += 4
    elif op == 4:
        valor_final += 6
    else:
        break
print(f'O total a ser pago é de R$ {valor_final:.2f}.')
