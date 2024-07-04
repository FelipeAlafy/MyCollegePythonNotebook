# Exercício referente a Aula 3 de Lógica de Programação e Algoritmos
# Autor: Felipe Alafy Rodrigues Silva
# Criado em: 02/07/2024
# Última Modificação em: 20/06/2024
# Acesse o side Notes no meu Notion:
# https://www.notion.so/PA-L-gica-de-Programa-o-e-Algoritmos-b81c5cb3551e4a62b9b2c5b8b58fc2ac?pvs=4

# Condicional simples
# Traduza as afirmações a seguir para condicionais em Python
print('a) Se idade é maior que 60, escreva: "Você tem direitos aos benefícios"')
idade = int(input('Digite sua idade: '))
if idade > 60:
    print('Você tem direito aos benefícios')
else:
    print('Você é jovem de mais, ainda.')

print('b) Se dano é maior que 10 e escudo é igual a O \"Você está morto!\"')
escudo = int(input('Digite um valor para escudo: '))
dano = int(input('Digite um valor para dano: '))
if escudo == 0 and dano > 10:
    print('Você está morto!')
else:
    print('Você sobreviveu')

print('c) Se pelo menos uma das variáveis booleanas norte, sul, leste e oeste resultarem em True, escreva: "Você '
      'escapou!"')

norte = False
sul = True
leste = False
oeste = True
if norte or sul or leste or oeste:
    print('Você escapou!')
