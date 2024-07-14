# Exercício 2
# - Suponha que você é um colecionar de jogos de videogame. Escreva um algoritmo que
# permita cadastrar esses jogos informando o nome e a qual videogame ele pertence
# - Para isso, crie um menu de opções contendo:
# cadastrar novo item, listar tudo que foi cadastrado e sair

def menu():
    print('MENU'.center(50, '-'))
    print('1 - CADASTRAR NOVO JOGO')
    print('2 - LISTAR JOGOS SALVOS')
    print('3 - SAIR')
    x = -1
    while 0 > x < 4:
        try:
            x = int(input('Digite a opção desejada: '))
        except ValueError:
            print('Você não digitou uma opção númerica.')
        finally:
            print('-' * 50)
    return x


def cadastrar():
    print('MENU CADASTRAR'.center(50, '-'))

    jogo = ''
    while jogo == '' or len(jogo) < 3:
        try:
            print('O nome do jogo deve ter mais que 3 caracteres.')
            jogo = input('Digite o nome do jogo: ')
        except ValueError:
            print('Você digitou um caractere inválido, tente novamente.')

    videogame = ''
    while videogame == '' or len(videogame) < 1:
        try:
            print('O nome do videogame deve ter mais que 1 caractere.')
            videogame = input('Digite o nome do videogame: ')
        except ValueError:
            print('Você digitou um caractere inválido, tente novamente.')

    return f'O jogo {jogo} pertence ao videogame {videogame}\n'




while True:
    op = menu()
    if op == 1:
        arquivo_nome = 'pratica5_out.txt'
        arquivo = ''
        try:
            arquivo = open(arquivo_nome, mode='a+')
        except OSError:
            print('Um erro ocorreu ao tentar abrir o arquivo.')

        str = cadastrar()
        arquivo.write(str)
        arquivo.close()
    if op == 2:
        arquivo_nome = 'pratica5_out.txt'
        arquivo = ''
        try:
            arquivo = open(arquivo_nome, mode='r')
        except OSError:
            print('Um erro ocorreu ao tentar abrir o arquivo.')

        for line in arquivo:
            print(line)
        arquivo.close()
    if op == 3:
        break
