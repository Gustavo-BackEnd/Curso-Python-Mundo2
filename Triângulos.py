#Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de
# triângulo será formado:
#– EQUILÁTERO: todos os lados iguais
#– ISÓSCELES: dois lados iguais, um diferente
#– ESCALENO: todos os lados diferentes

print('=-' * 20)
print('Analisando triângulo')
print('=-' * 20)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2 :
    print(f'Conseguimos formar um triângulo com os segumentos {r1:.0f} {r2:.0f} {r3:.0f}')
    if r1 == r2 == r3:
        print('Esse é um triângulo EQUILÁTERO! Todos os lados são iguais.')
    elif r1 == r2:
        print('Esse é um triângulo ISÓSCELES! Tem dois lados iguais.')
    elif r2 == r3:
        print('Esse é um triângulo ISÓSCELES! Tem dois lados iguais.')
    elif r3 == r1:
        print('Esse é um triângulo ISÓSCELES! Tem dois lados iguais.')
    else:
        print('Esse é um triângulo ESCALENO! Todos os lados são diferentes.')
else:
    print(f'Não conseguimos formar um triângulo com os seguimento {r1} {r2} {r3}.')