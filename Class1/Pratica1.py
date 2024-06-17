# Conteúdo referente a Aula 1 de Lógica de Programação e Algoritmos
# Autor: Felipe Alafy Rodrigues Silva
# Criado em: 10/06/2024
# Última Modificação em: 11/06/2024
# Acesse o side Notes no meu Notion:
# https://www.notion.so/PA-L-gica-de-Programa-o-e-Algoritmos-b81c5cb3551e4a62b9b2c5b8b58fc2ac?pvs=4#d478ed82dd8d4c7683479d5ef03a7ef4

# Escreva as seguintes expressões algébricas em linguagem Python:
# a) O somatório dos 5 primeiros números inteiros e positivos
# b) A média entre 23, 19 e 31
# c) O número de vezes que 73 cabe em 403
# d) A sobra quando 403 é dividido por 73

print('-' * 60)
print('Exercicio 1 - letra A: O somatório dos 5 primeiros números\ninteiros e positivos')
# \n é o caractere reponsável por qubrar uma linha em uma mensagem, portanto podemos usar essa combinação \n para
# fazer isso em strings
somatorio = 1 + 2 + 3 + 4 + 5
print(f'1 + 2 + 3 + 4 + 5 = {somatorio}')

print('-' * 60)
print('Exercicio 1 - letra B: A média entre 23, 19 e 31')
media = (29 + 19 + 31) / 3
print(f'A média entre os três valores é igual à {media}')

print('-' * 60)
print('Exercicio 1 - letra C: O número de vezes que 73 cabe em 403')
quantidade_de_vezes_maior = 403 // 73
print(f'73 cabe {quantidade_de_vezes_maior} em 403')

print('-' * 60)
print('Exercicio 1 - letra d: A sobra quando 403 é dividido por 73')
sobra_da_divisao = 403 % 73
print(f'A sobra da divisão entre 403 e 73 é igual á {sobra_da_divisao}')
print('-' * 60)

# Escreva as seguintes expressões algébricas em linguagem Python:
# e) 2 elevado à 10ª potência
# f) O valor absoluto da diferença entre 54 e 57
# g) O menor valor entre 34, 29 e 31
print('Exercicio 1 - letra e: 2 elevado à 10ª potência')
valor_elevado = 2**10
print(f'O resultado é {valor_elevado}')
print('-' * 60)

print('Exercicio 1 - letra f: O valor absoluto da diferença entre 54 e 57')
valor_absoluto = abs(54 - 57)
# A função abs é responsável por obter o valor absoluto do resultado de uma operação matemática que resultaria em um
# valor negativo.
print(f'O resultado é {valor_absoluto}')
print('-' * 60)

print('Exercicio 1 - letra g: O menor valor entre 34, 29 e 31')
menor_valor = min(34, 29, 31)
# A função min() é a responsável por obter o menor valor dado uma lista de valores como seus argumentos
# Argumentos são os valores que passamos entre parenteses para uma função, podem ser chamados também de parametros
# De mesma forma existe também uma função max() que obtem o maior valor dada uma lista à ela.
print(f'O menor valor da lista é {menor_valor}')
print('-' * 60)

# Exercicio 2 - Atribuição
# Escreva as expressões em Python para:
# a) Atribuir o valor inteiro 3 à variável a
# b) Atribuir o valor 4 à variável b
# c) Atribuir à variável c o valor da expressão a*a + b * b

print('Exercicio 2 - letra a: Atribuir o valor inteiro 3 à variável a')
a = 3
print(f'O valor da variável a é {a}')
print('-' * 60)

print('Exercicio 2 - letra b: Atribuir o valor 4 à variável b')
b = 4
print(f'O valor da variável b é {b}')
print('-' * 60)

print('Exercicio 2 - letra c: Atribuir a variável c o valor da expressão a * a + b * b')
c = a * a + b * b
print(f'O valor da expressão numerica armazenada em c é igual {c}')
print('-' * 60)

# Exericio 3 - Strings:
# Execute as seguintes atribuições:
# sl = 'ant'
# s2 = 'bat'
# s3 = 'cod'

print("""Exercicio 3 - String: execute as seguntes atribuições:\nsl = 'ant'\ns2 = 'bat'\ns3 = 'cod'""")
sl = 'ant'
s2 = 'bat'
s3 = 'cod'
print('-' * 60)

# Exercicio 4 - Strings:
# - Agora, utilizando operadores + e *, crie as saídas
# a seguir:
# a) 'ant bat cod'
# b) 'ant ant ant ant ant ant ant ant ant ant'
# c) 'ant bat bat cod cod cod'
# d) 'ant bat ant bat ant bat ant bat ant bat ant bat ant bat'
# e) 'batbatcod batbatcod batbatcod batbatcod batbatcod'

print('Exercicio 4 - letra a: Agora, ultilizando operadores + e *, crie a saída: "ant bat cod"')
print(sl, s2, s3)
print('-' * 60)

print('Exercicio 4 - letra b: Agora, ultilizando operadores + e *, crie a saída: "ant ant ant ant ant ant ant ant ant '
      'ant"')
print(sl * 10)
print('-' * 60)

print('Exercicio 4 - letra c: Agora, ultilizando operadores + e *, crie a saída: "ant bat bat cod cod cod"')
print(f"{(sl + ' ') * 1}{(s2 + ' ') * 2}{(s3 + ' ') * 3}")
print('-' * 60)

print('Exercicio 4 - letra d: Agora, ultilizando operadores + e *, crie a saída: "ant bat ant bat ant bat ant bat ant '
      'bat ant bat ant bat"')
print((sl + ' ' + s2 + ' ') * 7)
print('-' * 60)

print('Exercicio 4 - letra e: Agora, ultilizando operadores + e *, crie a saída: "batbatcod batbatcod batbatcod '
      'batbatcod batbatcod"')
print((s2 + s2 + s3 + ' ') * 5)
print('-' * 60)
