#Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário
# escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.
num = int(input('Escreva um número inteiro: '))
print('''Escolha para qual base vai querer converter:
[1] para binário;
[2] para octal;
[3] para hexadecimal''')
resposta = int(input('Digite a opção desejada: '))
if resposta == 1:
    print(f'O número {num} convertido para binário é: {bin(num)[2:]}')
elif resposta == 2:
    print(f'O número {num} convertido para octal é: {oct(num)[2:]}')
elif resposta == 3:
    print(f'O número {num} convertido para hexadecimal é: {hex(num)[2:]}')
else:
    print('Opção inválida. Escolha uma opção entre 1, 2 ou 3')