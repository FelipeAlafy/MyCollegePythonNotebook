# Conteúdo referente a Aula 5 de Lógica de Programação e Algoritmos
# Autor: Felipe Alafy Rodrigues Silva
# Criado em: 07/07/2024
# Última Modificação em: 07/07/2024
# Acesse o side Notes no meu Notion:
# https://www.notion.so/PA-L-gica-de-Programa-o-e-Algoritmos-b81c5cb3551e4a62b9b2c5b8b58fc2ac?pvs=4
spaces = 70


# Declaração de uma função simples:
def menu():
    print('-' * spaces)
    print('                         MENU DE SERVIÇOS')
    print('-' * spaces)
    print('1 - Lavagem simples')
    print('2 - Lavagem de tecidos suave')
    print('3 - Lavagem simples + secagem')
    print('-' * spaces)


print('Selecione o tipo de serviço da lavanderia para a primeira máquina')
menu()
# primeira_opcao = int(input('>> '))

print('Selecione o tipo de serviço da lavanderia para segunda máquina')
menu()


# segunda_opcao = int(input('>> '))


# Função com parâmetro:
def menu(numero_maquina):
    print('-' * spaces)
    print('                         MENU DE SERVIÇOS')
    print('-' * spaces)
    print('1 - Lavagem simples')
    print('2 - Lavagem de tecidos suave')
    print('3 - Lavagem simples + secagem')
    print('-' * spaces)
    print(f'Selecione o tipo de serviço da lavanderia para a {numero_maquina}ª máquina')


menu(1)
# primeira_opcao = int(input('>> '))

menu(2)


# segunda_opcao = int(input('>> '))


# Função com mais de um parâmetro:
def sub(num1, num2):
    print(num1 - num2)


sub(10, 2)
# Resultado: 8

# Trocando os parâmetros na chamada
sub(num2=10, num1=2)


# Resultado: -8


# Função com parâmetro com valor padrão, default value.
def menu_default(numero_maquina=1):
    print('-' * spaces)
    print('                         MENU DE SERVIÇOS')
    print('-' * spaces)
    print('1 - Lavagem simples')
    print('2 - Lavagem de tecidos suave')
    print('3 - Lavagem simples + secagem')
    print('-' * spaces)
    print(f'Selecione o tipo de serviço da lavanderia para a {numero_maquina}ª máquina')


menu_default()
# primeira_opcao = int(input('>> '))

menu_default(2)
# segunda_opcao = int(input('>> '))


ovos = 2


def bacon():
    global ovos
    ovos = 10


bacon()
print(ovos)


def soma(num1, num2):
    return num1 + num2


print(soma(1, 1))

while True:
    try:
        x = float(input('Digite um valor númerico!\n>> '))
        break
    except ValueError:
        print('Você não inseriu um valor númerico, tente novamente!')


def div():
    try:
        num1 = int(input("Digite um número: "))
        num2 = int(input("Digite um número: "))
        res = num1 / num2
    except ZeroDivisionError:
        print("Oops!  Erro de divisão por zero...")
    except:
        print("Algo de errado aconteceu...")
    else:
        return res
    finally:
        print("Executará sempre!")


# programa principal

print(div())
