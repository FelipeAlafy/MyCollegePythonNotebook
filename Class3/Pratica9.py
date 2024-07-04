# Exercício referente a Aula 3 de Lógica de Programação e Algoritmos
# Autor: Felipe Alafy Rodrigues Silva
# Criado em: 02/07/2024
# Última Modificação em: 20/06/2024
# Acesse o side Notes no meu Notion:
# https://www.notion.so/PA-L-gica-de-Programa-o-e-Algoritmos-b81c5cb3551e4a62b9b2c5b8b58fc2ac?pvs=4

# Condicional composta - Traduza as afirmações a seguir para condicionais em Python •
import datetime

print('a) Se ano é divisível por 4, escreva: "Pode ser um ano bissexto". Caso contrário, escreva: "Definitivamente '
      'não é um ano bissexto"')

date = datetime.datetime.now()
print(date.year)
if date.year % 4 == 0 and date.year % 100:
    print('É um ano bissexto.')
else:
    print('Definitivamente não é um ano bissexto.')

# • b) Se ambas as variáveis booleanas cima e baixo forem True, escreva: "Decida-se!" caso contrário, escreva:
# "Você escolheu um caminho!"
cima = True
baixo = False
if cima and baixo:
    print('Decida-se!')
else:
    print('Você escolheu um caminho!')
