# Conteúdo referente a Aula 4 de Lógica de Programação e Algoritmos
# Autor: Felipe Alafy Rodrigues Silva
# Criado em: 27/06/2024
# Última Modificação em: 27/06/2024
# Acesse o side Notes no meu Notion:
# https://www.notion.so/PA-L-gica-de-Programa-o-e-Algoritmos-b81c5cb3551e4a62b9b2c5b8b58fc2ac?pvs=4

# Exercício com acumulador
# - Escreva um algoritmo que calcule a sua média de notas em determinada disciplina Vamos assumir
# que a média final é dada pela média aritmética de cinco notas digitadas

soma = 0
counter = 1
while counter < 6:
    soma = soma + float(input(f'Digite a nota {counter}ª do(a) aluno(a): '))
    counter = counter + 1

media = soma/5
print(f'A média final do(a) aluno(a) foi de {media:.2f}')
