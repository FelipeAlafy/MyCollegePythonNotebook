# Conteúdo referente a Aula 4 de Lógica de Programação e Algoritmos
# Autor: Felipe Alafy Rodrigues Silva
# Criado em: 26/06/2024
# Última Modificação em: 27/06/2024
# Acesse o side Notes no meu Notion:
# https://www.notion.so/PA-L-gica-de-Programa-o-e-Algoritmos-b81c5cb3551e4a62b9b2c5b8b58fc2ac?pvs=4

n = 1
counter = 1
while counter < 6:
    print(n)
    counter += 1

print('Terminei o laço')

print('-' * 40)
continuar = 's'
while continuar.lower() == 's':
    x = input('Digite algo: ')
    print(x)
    continuar = input('Deseja continuar s/n? ')

# Mesmo exemplo acima porém reescrito com while True
# while True:
#   x = input('Digite algo: ')
#    print(x)
#    continuar = input('Deseja continuar s/n? ')
#    if continuar.lower() == 'n':
#        break

print('-' * 40)
s = 1
c = 1
while c < 6:
    s = s + c
    print(s)
    c = c + 1

count = 0
while True:
    v = int(input('Digite um valor maior que zero e positivo: '))
    if v:
        print(f'Você digitou {v}, fechando o programa.')
        break
    else:
        print('Você digitou zero, tente novamente.')
        print(f'Você já errou {count} vezes')
        continue
        # count += 1

print('-'*40)
print('Loop For:')
for i in range(0, 10):
    print(i)

print('-'*40)
for i in range(10, -1, -2):
    print(i)

frase = 'Lógica de Programação e Algoritmos'
for i in range(0, len(frase), 2):
    print(frase[i])

for index, i in enumerate(frase):
    if index % 2 == 0:
        print(i)
