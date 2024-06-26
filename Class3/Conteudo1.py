# Conteúdo referente a Aula 3 de Lógica de Programação e Algoritmos
# Autor: Felipe Alafy Rodrigues Silva
# Criado em: 19/06/2024
# Última Modificação em: 19/06/2024
# Acesse o side Notes no meu Notion:
# https://www.notion.so/PA-L-gica-de-Programa-o-e-Algoritmos-b81c5cb3551e4a62b9b2c5b8b58fc2ac?pvs=4

print('Aula 3 - Lógica de Programação e Algoritmos')
print('Conteúdo deste arquivo, If, Else')
print('-' * 40)

print('Usando apenas If:')
numero1 = int(input('Digite o primeiro valor: '))
numero2 = int(input('Digite o segundo valor: '))
if numero1 > numero2:
    print(f'{numero1} é maior que {numero2}')
if numero2 > numero1:
    print(f'{numero2} é maior que {numero1}')

print('-' * 40)
print('Usando If e Else:')
if numero1 > numero2:
    print(f'{numero1} é maior que {numero2}')
else:
    print(f'{numero2} é maior que {numero1}')

print('-' * 40)
print('Usando If, Elif e Else:')
if numero1 > numero2:
    print(f'{numero1} é maior que {numero2}')
elif numero1 == numero2:
    print(f'{numero1} é igual a {numero2}')
else:
    print(f'{numero2} é maior que {numero1}')

print('-' * 40)
print(f'O número {numero1}')
if numero1 % 2 == 0:
    print(' é par.')
else:
    print(' é ímpar.')
