# Exercício referente a Aula 3 de Lógica de Programação e Algoritmos
# Autor: Felipe Alafy Rodrigues Silva
# Criado em: 20/06/2024
# Última Modificação em: 20/06/2024
# Acesse o side Notes no meu Notion:
# https://www.notion.so/PA-L-gica-de-Programa-o-e-Algoritmos-b81c5cb3551e4a62b9b2c5b8b58fc2ac?pvs=4

# Exercício: Um aluno, para passar de ano, precisa ser aprovado em todas as matérias que está cursando Assuma que a
# média para aprovação é a partir de 7 e que o aluno cursa 3 matérias, somente. Escreva um algoritmo que leia a nota
# final do aluno em cada matéria e informe, na tela, se ele passou de ano ou não (Menezes, 2019, p. 60)

print("""Um aluno, para passar de ano, precisa ser aprovado em todas as matérias que está cursando Assuma que a
média para aprovação é a partir de 7 e que o aluno cursa 3 matérias, somente. Escreva um algoritmo que leia a nota
final do aluno em cada matéria e informe, na tela, se ele passou de ano ou não""")

print('-' * 40)

nota_final_materia1 = float(input('Digite a nota final na primeira materia: '))
nota_final_materia2 = float(input('Digite a nota final na segunda materia: '))
nota_final_materia3 = float(input('Digite a nota final na terceira materia: '))

print('-' * 40)

if nota_final_materia1 >= 7 and nota_final_materia2 >= 7 and nota_final_materia3 >= 7:
    print('O aluno foi aprovado de ano por média.')
else:
    print('O aluno foi reprovado por média.')
