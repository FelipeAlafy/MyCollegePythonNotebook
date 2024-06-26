# Conteúdo referente a Aula 2 de Lógica de Programação e Algoritmos
# Autor: Felipe Alafy Rodrigues Silva
# Criado em: 10/06/2024
# Última Modificação em: 11/06/2024
# Acesse o side Notes no meu Notion:
# https://www.notion.so/PA-L-gica-de-Programa-o-e-Algoritmos-b81c5cb3551e4a62b9b2c5b8b58fc2ac?pvs=4

# Exercício 1:
# Desenvolva um algoritmo que solicite ao usuário o preço de um produto e um percentual de desconto a
# ser aplicado a ele. Calcule e exiba o valor do desconto e o preço final do produto.

preco = float(input('Por favor, digite o preço do produto: '))
porcentagem_de_desconto = float(input('Por favor, digite a porcentagem do desconto à ser aplicado: '))

preco_pos_desconto_aplicado = preco - ((preco * porcentagem_de_desconto) / 100)
print(f'O novo preço com desconto de {porcentagem_de_desconto:.1f}'
      f' aplicado, passa a ser R$ {preco_pos_desconto_aplicado:.2f}')
