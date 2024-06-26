# Exercício referente a Aula 3 de Lógica de Programação e Algoritmos
# Autor: Felipe Alafy Rodrigues Silva
# Criado em: 20/06/2024
# Última Modificação em: 20/06/2024
# Acesse o side Notes no meu Notion:
# https://www.notion.so/PA-L-gica-de-Programa-o-e-Algoritmos-b81c5cb3551e4a62b9b2c5b8b58fc2ac?pvs=4

# Escreva um algoritmo que leia um nome e uma idade Caso o nome digitado seja Vinicius, escreva isso na tela
# Caso o usuário digite qualquer outro nome, verifique sua idade. Se for menor que 18 anos,
# informe que é de menor. Se for maior que 100 anos, informe que esta pessoa possivelmente não eb(iste

nome = input('Digite um nome: ')
idade = int(input('Digite uma idade: '))

if nome.lower() == 'vinicius':
    print(nome)
    exit(0)

if idade < 18:
    print('você é menor de idade')
elif idade >= 100:
    print('Você possivelmente está morto.')
else:
    print('você é de maior de idade.')
