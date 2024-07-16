# Conteúdo referente a Aula 4 de Lógica de Programação e Algoritmos
# Autor: Felipe Alafy Rodrigues Silva
# Criado em: 27/06/2024
# Última Modificação em: 27/06/2024
# Acesse o side Notes no meu Notion:
# https://www.notion.so/PA-L-gica-de-Programa-o-e-Algoritmos-b81c5cb3551e4a62b9b2c5b8b58fc2ac?pvs=4

# Exercício
# Escreva um algoritmo em Python que calcule a tabuada de todos os números de 1 até 10, e, para cada
# número, vamos calcular a tabuada multiplicando-o pelo intervalo de 1 até 10

for i in range(1, 11):
    for c in range(0, 11):
        print(f' {i} x {c} = {i * c}')
    print('+', '-' * 14, '+')
