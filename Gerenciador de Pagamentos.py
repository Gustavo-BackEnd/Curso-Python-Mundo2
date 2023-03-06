valor = float(input('Preço das compras: '))
print('FORMAS DE PAGAMENTO:')
print('[1] à vista/cheque')
print('[2] à vista cartão')
print('[3] 2x no cartão')
print('[4] 3x no cartão ou mais')
opcao = int(input('Qual a opção de pagamento: '))

if opcao == 1:
     total = valor - (valor * 10 / 100)
     print(f'Para pagamento a vista tem 10% de desconto. Dando um total de R${total}.')
elif opcao == 2:
    total = valor - (valor * 5 / 100)
    print(f'Para pagamento a vista no cartão tem 5% de desconto. Dando um total de R${total}.')
elif opcao == 3:
    total = valor / 2
    print(f'Parcelado em 2x não corre juros. Dando um total de  R${valor}.')
elif opcao == 4:
    total = (valor * 20 / 100) + valor
    print(f'Parcelado em 3x ou mais tem um juros de 20%. Dando um total de R${total}.')