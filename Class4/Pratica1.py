# Conteúdo referente a Aula 4 de Lógica de Programação e Algoritmos
# Autor: Felipe Alafy Rodrigues Silva
# Criado em: 27/06/2024
# Última Modificação em: 27/06/2024
# Acesse o side Notes no meu Notion:
# https://www.notion.so/PA-L-gica-de-Programa-o-e-Algoritmos-b81c5cb3551e4a62b9b2c5b8b58fc2ac?pvs=4

# Exercício com contador
# Escreva um algoritmo que imprima na tela somente valores dentro de um intervalo especificado pelo
# usuário e que sejam número pares

inicio = int(input('Digite o valor inicial: '))
final = int(input('Digite o valor final: '))
final = final + 1
counter = inicio

while counter < final:
    if counter % 2 == 0:
        print(counter)
    counter = counter + 1
