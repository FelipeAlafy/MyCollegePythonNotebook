import math
# Exercício referente a Aula 3 de Lógica de Programação e Algoritmos
# Autor: Felipe Alafy Rodrigues Silva
# Criado em: 02/07/2024
# Última Modificação em: 20/06/2024
# Acesse o side Notes no meu Notion:
# https://www.notion.so/PA-L-gica-de-Programa-o-e-Algoritmos-b81c5cb3551e4a62b9b2c5b8b58fc2ac?pvs=4

# Exercício 1
# Faça um algoritmo que receba três valores, representando os lados de um triângulo fornecidos pelo usuário.
# Verifique se os valores formam um triângulo e classifique como
# • a) Equilátero (três lados iguais)
# • b) Isósceles (dois lados iguais)
# • c) Escaleno (três lados diferentes)
cateto_oposto = int(input("Digite o valor do cateto oposto: "))
cateto_adjascente = int(input("Digite o valor do cateto adjascente: "))
hipotenusa = int(input("Digite o valor da hipotenusa: "))

hipotenusa_real = math.sqrt(cateto_adjascente**2 + cateto_oposto**2)
if (cateto_oposto and cateto_adjascente and hipotenusa != 0) and (cateto_adjascente + cateto_oposto > hipotenusa and
                                                                  cateto_oposto + hipotenusa > cateto_adjascente and
                                                                  cateto_adjascente + hipotenusa > cateto_oposto):
    if cateto_oposto == cateto_adjascente == hipotenusa:
        print('Forma um triângulo equilátero.')
    elif cateto_adjascente != cateto_oposto != hipotenusa:
        print('Forma um triângulo Escaleno.')
    else:
        print('forma um triângulo Isósceles.')
else:
    print(f'Não forma um triângulo, sua hipotenusa deveria ser {hipotenusa_real}.')
