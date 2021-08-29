#_______________________TABUADA USANDO LAÇO WHILE___________________________#


#_________________________IMPORTANDO BIBLIOTECAS____________________________#
from os import system
from cabecalho import azul_claro, apresentacao, azul, roxo, vermelho, tracejado

#______________________________TABUADA 2.0__________________________________#


while True:
    apresentacao()
    try:
        sair = ' '   
        num = int(input(('Qual tabuada quer visualizar? ')))  
        azul('{:=^40}'.format(' TABUADA DO ' + str(num) + ' ') )
        for i in range(1, 11):
            azul_claro(f'{num} x {i:2} = {num*i}')      
        while sair not in 'sn':
            sair = str(input('Deseja continuar: [S/N] ')).lower().strip()[0]
            system('cls')      
        if sair == 'n':
            break
    except:
        vermelho('DIGITE APENAS NÚMEROS...')
        sair = str(input('Deseja continuar: [S/N] ')).lower().strip()[0]
    
tracejado()
roxo('{:^40}'.format(' FIM DO PROGRAMA ' ))
tracejado()





    

