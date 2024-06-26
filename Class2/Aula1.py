# Conteúdo referente a Aula 2 de Lógica de Programação e Algoritmos
# Autor: Felipe Alafy Rodrigues Silva
# Criado em: 10/06/2024
# Última Modificação em: 11/06/2024
# Acesse o side Notes no meu Notion:
# https://www.notion.so/PA-L-gica-de-Programa-o-e-Algoritmos-b81c5cb3551e4a62b9b2c5b8b58fc2ac?pvs=4

print("Olá, Mundo!")

print(2+2)
texto = "Olá, Mundo!"

print(texto)
print('-' * 40)

print('Operadores lógicos:')
numero1 = 2
numero2 = 4

resposta = numero1 == numero2
print(f'numero1 == numero2, {resposta}')

resposta = numero1 != numero2
print(f'numero1 != numero2, {resposta}')

resposta = numero1 <= numero2
print(f'numero1 <= numero2, {resposta}')

resposta = numero1 >= numero2
print('numero1 >= numero2, {}'.format(resposta))

print('-' * 40)
media = (numero1 + numero2) / 2
print('A média entre os dois valores é %.2f' % media)

print('-' * 40)
print('Manipulação de strings:')
x = 'Felipe'
print(f'vamos usar a string {x}')
a = x[2:4]
print(a)

a = x[2:]
print(a)

a = x[:2]
print(a)

a = x[::]
print(a)

print('O Tamanho de a e x são: {}, {}'.format(len(a), len(x)))

print('-' * 40)
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2
print('A média desse aluno foi %.2f' % media)
