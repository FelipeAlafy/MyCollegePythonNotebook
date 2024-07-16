# Conteúdo referente a Aula 5 de Lógica de Programação e Algoritmos
# Autor: Felipe Alafy Rodrigues Silva
# Criado em: 14/07/2024
# Última Modificação em: 14/07/2024
# Acesse o side Notes no meu Notion:
# https://www.notion.so/PA-L-gica-de-Programa-o-e-Algoritmos-b81c5cb3551e4a62b9b2c5b8b58fc2ac?pvs=4

# Exercício 1
# - Escreva uma função que calcule o fatorial de um número recebido como parâmetro e
# retorne o seu resultado
# - Faça uma validação dos dados por meio de uma outra função, permitindo que somente
# valores positivos sejam aceitos
# - Crie o help da sua função (exercício da apostila — aula 5)

def valida(valor):
    """
    Essa função válida um valor númerico recebido é positivo.

    :param valor: valor à ser validado
    :return: retorna verdadeiro ou falso, a depender do sucesso da validação.
    """

    if valor > 0:
        return True
    return False


def fatorial(valor):
    """
    Está função retorna o fatorial de um número, é feito um laço
    enquato o parâmetro é maior que 0, o valor é multiplicado
    pelo da valor da variável resultado, com valor inicial de 1,
    posteriormente é feito a atribuição do novo valor para a variável
    resultado.

    :param valor: recebe o valor inicial do fatorial
    :return: é retornado o valor final da iteração obtida no laço enquanto.
    """

    if not valida(valor):
        print(f'Impossível de fazer o fatorial de {valor}, pois não é positivo ou é zero.')
        return 0

    resultado = 1
    while valor > 0:
        resultado *= valor
        valor -= 1
    return resultado


help(valida)
help(fatorial)

x = 0
try:
    x = int(input('Digite um valor para calcular o fatorial: '))
    print(f'{x}! = {fatorial(x)}')
except ValueError:
    print('Você não digitou um valor tente novamente.')
except TypeError:
    print('Você não digitou um valor inteiro, operação não permitida, tente novamente.')
