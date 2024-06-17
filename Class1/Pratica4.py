# Conteúdo referente a Aula 1 de Lógica de Programação e Algoritmos
# Autor: Felipe Alafy Rodrigues Silva
# Criado em: 11/06/2024
# Última Modificação em: 11/06/2024
# Acesse o side Notes no meu Notion:
# https://www.notion.so/PA-L-gica-de-Programa-o-e-Algoritmos-b81c5cb3551e4a62b9b2c5b8b58fc2ac?pvs=4#d478ed82dd8d4c7683479d5ef03a7ef4

# Exercício 3
# Crie uma variável de string que receba uma  frase qualquer. Crie uma Segunda variável, agora contendo a
# metade da string digitada. Imprima na tela somente os dois últimos caracteres da segunda variável do tipo string

frase = str(input('Digite uma frase qualquer: '))
tamanho = len(frase)
metade_da_frase = frase[:int(tamanho/2)]
print(metade_da_frase[1:])
