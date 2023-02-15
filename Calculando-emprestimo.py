#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
#Pergunte o valor da casa, o salário do comprador e em quantos meses ele vai pagar.
#A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

casa = float(input('Qual o valor do imóvel? '))
salario = float(input('Qual o seu salário mensal? '))
parcelas = int(input('Quantos meses deseja parcelar? '))
divisao = casa / parcelas

if divisao > salario*30/100:
    print('Desculpe, o seu empréstimo foi negado.')
else:
    print('Parabéns, seu empréstimo foi aprovado.')

