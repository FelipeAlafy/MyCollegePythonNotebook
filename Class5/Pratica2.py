# Conteúdo referente a Aula 5 de Lógica de Programação e Algoritmos
# Autor: Felipe Alafy Rodrigues Silva
# Criado em: 07/07/2024
# Última Modificação em: 07/07/2024
# Acesse o side Notes no meu Notion:
# https://www.notion.so/PA-L-gica-de-Programa-o-e-Algoritmos-b81c5cb3551e4a62b9b2c5b8b58fc2ac?pvs=4

# Exercício 2
# Escreva uma função para validar uma string. Essa função recebe como parâmetro a string,
# o número mínimo e máximo de caracteres. Retorne verdadeiro se o tamanho da string
# estiver entre os valores de mínimo e máximo, e falso, caso contrário (elaborado com base em Menezes, s. d.)

def valida_string(pergunta, min, max):
    texto = input(pergunta)
    tamanho = len(texto)
    while min > tamanho < max:
        texto = input(pergunta)
        tamanho = len(texto)
    return texto


x = valida_string('digite um texto maior que 10 e menor que 20 caracters\n>> ', 10, 20)
print(x)
