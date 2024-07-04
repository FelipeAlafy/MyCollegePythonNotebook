# Exercício referente a Aula 3 de Lógica de Programação e Algoritmos
# Autor: Felipe Alafy Rodrigues Silva
# Criado em: 04/07/2024
# Última Modificação em: 20/06/2024
# Acesse o side Notes no meu Notion:
# https://www.notion.so/PA-L-gica-de-Programa-o-e-Algoritmos-b81c5cb3551e4a62b9b2c5b8b58fc2ac?pvs=4

# Exercício 3
# Escreva um programa que calcule o preço a pagar pelo fornecimento de energia elétrica. Pergunte a quantidade
# de kWh consumida e o tipo de instalação: R para residências, I para indústrias e C para comércios

print('Calculadora de consumo de energia elétrica')
print('-'*60)
print('R para residências\nI para indústrias\nC para comércios')
tipo_instalacao = input('Digite o tipo de sua instalação: ')
qtd_kw_h_consumido = float(input('Digite a quantidade de kW/h consumidos no seu padrão elétrico: '))

valor_do_kwh = 0
if tipo_instalacao == 'R' and qtd_kw_h_consumido <= 500:
    valor_do_kwh = 0.4
elif tipo_instalacao == 'R' and qtd_kw_h_consumido > 500:
    valor_do_kwh = 0.65
elif tipo_instalacao == 'C' and qtd_kw_h_consumido <= 1000:
    valor_do_kwh = 0.55
elif tipo_instalacao == 'C' and qtd_kw_h_consumido > 1000:
    valor_do_kwh = 0.60
elif tipo_instalacao == 'I' and qtd_kw_h_consumido <= 5000:
    valor_do_kwh = 0.55
elif tipo_instalacao == 'I' and qtd_kw_h_consumido > 5000:
    valor_do_kwh = 0.60
else:
    print('Tipo de instalação inexistente.')
    exit(0)

print(f'O valor da sua conta será aproximadamente de R$ {valor_do_kwh * qtd_kw_h_consumido:.2f}')
