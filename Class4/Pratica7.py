# Conteúdo referente a Aula 4 de Lógica de Programação e Algoritmos
# Autor: Felipe Alafy Rodrigues Silva
# Criado em: 15/07/2024
# Última Modificação em: 15/07/2024
# Acesse o side Notes no meu Notion:
# https://www.notion.so/PA-L-gica-de-Programa-o-e-Algoritmos-b81c5cb3551e4a62b9b2c5b8b58fc2ac?pvs=4
# Exercício 3
# Um cinema cobra preços diferentes para os ingressos, de acordo com a idade da pessoa. Se a pessoa tiver menos de 3
# anos de idade, o ingresso será gratuito; se tiver entre 3 e 12 anos, o ingresso custará R$ 15; se tiver mais de
# 12 anos, custará R$ 30
# Escreva um laço em que você pergunte a idade aos usuários e, então, informe-lhes o
# preço do ingresso do cinema Encerre o laço, usando um break quando o usuário digitar zero
# Após encerrar o laço, apresente na tela o total de pessoas que compraram ingressos, o total de dinheiro arrecadado
# e a média de idade das pessoas

print('Cinema'.center(50, '-'))
print('digite a idade para comprar um ingresso')
print('Pessoas com menos de 3 anos não pagam o ingresso.')
print('Pessoas com idade entre 3 e 12 anos pagam 15 reais de ingresso.')
print('Pessoas com idade maior que 12 anos pagam 30 reais de ingresso.')
print('-'*50)
qtd_ingressos_vendidos = 0
dinheiro = 0
soma_idades = 0
while True:
    idade = int(input('Digite a idade, 0 para encerrar:\n>> '))
    if idade <= 0:
        break
    elif 0 < idade < 3:
        dinheiro += 0
        qtd_ingressos_vendidos += 1
        soma_idades += idade
    elif 3 <= idade <= 12:
        dinheiro += 15
        qtd_ingressos_vendidos += 1
        soma_idades += idade
    else:
        dinheiro += 30
        qtd_ingressos_vendidos += 1
        soma_idades += idade
    print(dinheiro)

if qtd_ingressos_vendidos != 0:
    print(f'O total de pessoas que compraram foi {qtd_ingressos_vendidos}\nFoi arrecado: R$ {dinheiro:.2f}\n'
          f'Á média da idade das pessoas é de {soma_idades/qtd_ingressos_vendidos}')
