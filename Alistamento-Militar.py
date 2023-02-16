#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
# se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do
# tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo
from datetime import date
ano = date.today().year
ano_nasc = int(input('Ano de nascimento? '))
idade = ano - ano_nasc

if idade == 18:
    print(f'Você tem {idade} anos. Está no perído do seu alistamento.')
elif idade > 18:
    atrasado = idade - 18
    print(f'Você tem {idade} anos. Já passou {atrasado} anos do período de alistamento. Está atrasado.')
    ano_alis = ano - atrasado
    print(f'Seu alistamento foi em {ano_alis}')
elif idade < 18:
    print(f'Você tem {idade} anos. Ainda está muito novo. Faltam {18-idade} anos para se alistar')
    ano_alis = 18 - idade + ano
    print(f'Seu ano de alistamento será em {ano_alis}')