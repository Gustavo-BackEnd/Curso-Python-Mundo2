#A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um
# atleta e mostre sua categoria, de acordo com a idade:
#– Até 9 anos: MIRIM
#– Até 14 anos: INFANTIL
#– Até 19 anos: JÚNIOR
#– Até 25 anos: SÊNIOR
#– Acima de 25 anos: MASTER

from datetime import date
ano = date.today().year
ano_nasci = int(input('Qual o ano do seu nascimento? '))
idade = ano - ano_nasci

if idade <= 9:
    print(f'Você tem {idade} anos, portanto é um atleta MIRIM!')
elif 14 >= idade > 9:
    print(f'Você tem {idade} anos, portanto é um atleta INFANTIL!')
elif 19 >= idade > 14:
    print(f'Você tem {idade} anos, portanto é um atleta JUNIOR')
elif 25 >= idade > 19:
    print(f'Você tem {idade} anos, portanto é um atleta SÊNIOR!')
else:
    print(f'Você tem {idade} anos, portanto é um atleta MASTER!')