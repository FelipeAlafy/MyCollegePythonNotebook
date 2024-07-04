# Exercício referente a Aula 3 de Lógica de Programação e Algoritmos
# Autor: Felipe Alafy Rodrigues Silva
# Criado em: 02/07/2024
# Última Modificação em: 20/06/2024
# Acesse o side Notes no meu Notion:
# https://www.notion.so/PA-L-gica-de-Programa-o-e-Algoritmos-b81c5cb3551e4a62b9b2c5b8b58fc2ac?pvs=4

# Escreva as seguintes expressões booleanas em linguagem Python
#
print("a) 1387 é divisível por 19")
if 1387 % 19 == 0:
    print("É divisível")
else:
    print("Não é divisível")

print("b) 31 é par")
if 31 % 2 == 0:
    print("É par")
else:
    print("Não é par")

print("c) O menor valor entre: 34, 29 e 31 é menor que 30")
if min(34, 29, 31) < 30:
    print("Verdade")
else:
    print("Mentira")
