# Conteúdo referente a Aula 4 de Lógica de Programação e Algoritmos
# Autor: Felipe Alafy Rodrigues Silva
# Criado em: 26/06/2024
# Última Modificação em: 26/06/2024
# Acesse o side Notes no meu Notion:
# https://www.notion.so/PA-L-gica-de-Programa-o-e-Algoritmos-b81c5cb3551e4a62b9b2c5b8b58fc2ac?pvs=4

# Exercício:
# Escreva um algoritmo que calcule a média dos números pares de 1 até 100 (1 e 100 inclusos).
# Implemente o laço usando for:

soma = 0
counter = 0
media = 0
for i in range(0, 101, 2):
    counter += 1
    soma += i

media = soma / counter
print(f'A média é {media}')
