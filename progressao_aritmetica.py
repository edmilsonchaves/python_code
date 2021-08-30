#_______________________________________________________________________#
# Name: "Progressão Aritmética"
# Version: "1.0.0"
# Description: "Progressão aritmética"
# Author: edmilsonchaves
# Language: pt-br
#_________________________IMPORTANDO BIBLIOTECAS________________________#

from os import system
from time import sleep
#_________________________PROGRESSÃO ARITMÉTICA_________________________#

while True:
    try:    
        print('='* 30)
        print('{:^30}'.format('PROGRESSÃO ARITMÉTICA'))
        print('='* 30)

        termo = int(input('Qual o termo: '))
        pa = int(input('Qual a razão: '))
        qtd = int(input('Quantas progressões quer visualizar: '))
        contador = 1

        while contador <= qtd:
            print(f'{termo} → ', end=' ')
            termo += pa
            contador += 1
        print('FIM')
        sair = ' '
        while sair not in 'sn':
            sair = str(input('Deseja continuar: [S/N] ')).lower().strip()[0]
            system('cls')
        if sair == 'n':
            break
    except:
        print('ALERTA! Informe apenas números...')
        sleep(2)
        system('cls')

print('FIM DO PROGRAMA')

