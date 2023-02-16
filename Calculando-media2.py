# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem
# no final, de acordo com a média atingida:
#– Média abaixo de 5.0: REPROVADO
#– Média entre 5.0 e 6.9: RECUPERAÇÃO
#– Média 7.0 ou superior: APROVADO
nota1 = float(input('Qual a sua primeira nota? '))
nota2 = float(input('Qual a sua segunda nota? '))
media = (nota1 + nota2) / 2

if media < 5:
    print(f'Sua média foi {media:.1f}, ela é menor do que 5.')
    print(f'Você foi REPROVADO.')
elif media >= 7:
    print(f'Sua média foi {media:.1f}, ela é maior do que 7.')
    print('Parabéns você foi APROVADO.')
elif 7 > media >= 5:
    print(f'Sua média foi {media:.1f}, precisa tirar uma nota maior que 7.')
    print(f'Está de RECUPERAÇÃO.')

