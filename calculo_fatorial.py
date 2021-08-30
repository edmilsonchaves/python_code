# --------------------------------------------------------------------- #
# Name: "Cálculo de fatorial"
# Version: "1.0.0"
# Description: "Realiza o cálculo fatorial"
# Author: edmilsonchaves
# Language: pt-br
# --------------------------------------------------------------------- #
from math import factorial

while True:
    try:
        num = int(input('Digite um número para visualizar seu fatorial: '))
        fatorial = factorial(num)
        i = num
        print(f'{num}! ',end='')
        while i > 0:
            print(f'{i} ', end='')
            print('x ' if i > 1 else ' = ', end='')
            i-= 1
        print(fatorial)
        sair = ' '
        while sair not in 'sn':
            sair = str(input('Deseja visualizar outro fatorial: [S/N] ')).lower().strip()[0]
        if sair == 'n':
            break
    except:
        print('ERRO! DIGITE APENAS NÚMEROS')






















