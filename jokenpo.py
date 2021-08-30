#________________________IMPORTANDO BIBLIOTECAS____________________________

from random import randint
from time import sleep
from os import system
#_________________________CÓDIGO DO PROGRAMA________________________________


opcao = ('PEDRA', 'PAPEL', 'TESOURA')
validacao = 0, 1, 2
cont_jogador = cont_computador = 0

while True:
    computador = randint(0, 2)
    print('-='* 31)
    print('{:^61}'.format('J O K E N P Ó'))
    print('-='* 31)
    print('{:^61}'.format('R E G R A S'))
    print('PEDRA VENCE TESOURA | PAPEL VENCE PEDRA | TESOURA VENCE PAPEL')
    print('-='* 31)
    print('[0] - PEDRA\n[1] - PAPEL\n[2] - TESOURA')
    print('-='* 31)         
    try:
        jogador = int(input('Qual a sua jogada: '))
        while jogador not in validacao:
            jogador = int(input('OPÇÃO INVÁLIDA... Digite apenas 0 → 1 → 2: ')) 
            if jogador == str:
                jogador = int(input('NÃO DIGITE LETRAS, APENAS NÚMEROS 0 → 1 → 2: '))  
        print(f'{jogador} → {opcao[jogador]}')
        print('-='* 31)
        print('JO')
        sleep(1)
        print('KEN')
        sleep(1)
        print('PÓ')
        sleep(1)
        print('-='* 31)               
        if computador == 0: # computador escolhe PEDRA
            if jogador == 0:
                print('EMPATE!')
                print(f'JOGADOR JOGOU {opcao[0]} VS COMPUTADOR JOGOU {opcao[0]}')
            elif jogador == 1:
                print('JOGADOR VENCE!')
                print(f'JOGADOR JOGOU {opcao[1]} VS COMPUTADOR JOGOU {opcao[0]}')
                cont_jogador += 1
            elif jogador == 2:
                print('JOGADOR PERDEU | COMPUTADOR VENCE!')
                print(f'JOGADOR JOGOU {opcao[2]} VS COMPUTADOR JOGOU {opcao[0]}')
                cont_computador += 1
           
        if computador == 1: # Computador escolhe PAPEL
            if jogador == 0:
                print('JOGADOR PERDE | COMPUTADOR VENCE!')
                print(f'JOGADOR JOGOU {opcao[0]} VS COMPUTADOR JOGOU {opcao[1]}')
                cont_computador += 1
            elif jogador == 1:
                print('EMPATE')
                print(f'JOGADOR JOGOU {opcao[1]} VS COMPUTADOR JOGOU {opcao[1]}')
            elif jogador == 2:
                print('JOGADOR VENCE!')
                print(f'JOGADOR JOGOU {opcao[2]} VS COMPUTADOR JOGOU {opcao[1]}')
                cont_jogador += 1
         
        if computador == 2: # Computador escolhe TESOURA
            if jogador == 0:
                print('JOGADOR VENCE!')
                print(f'JOGADOR JOGOU {opcao[0]} VS COMPUTADOR JOGOU {opcao[2]}')
                cont_jogador += 1
            elif jogador == 1:
                print('JOGADOR PERDE!')
                print(f'JOGADOR JOGOU {opcao[1]} VS COMPUTADOR JOGOU {opcao[2]}')
                cont_computador += 1
            elif jogador == 2:
                print('EMPATE!')
                print(f'JOGADOR JOGOU {opcao[2]} VS COMPUTADOR JOGOU {opcao[2]}')
           
        sair = ' '    
        while sair not in 'sn':
            sair = str(input('Deseja continuar: [S/N] ')).lower().strip()[0]
            system('cls')
        if sair == 'n':
            break
    except:
        print('ERRO! NÃO DIGITAR LETRAS, APENAS NÚMEROS...')
        sleep(3)
        system('cls')
print('{:=^61}'.format(' PLACAR '))
print('{:>27} {:^} '.format('JOGADOR', cont_jogador), end='x')
print(f' {cont_computador:<} COMPUTADOR')

if cont_jogador > cont_computador:
      print('{:^61}'.format('JOGADOR VENCEU')) 
elif cont_jogador < cont_computador:
     print('{:^61}'.format('COMPUTADOR VENCEU')) 
else:
    print('{:^61}'.format('EMPATE')) 
print('='* 61)   

        
    
         
    
        


