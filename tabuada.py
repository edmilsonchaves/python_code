"""
Fazer um programa de tabuada usando laço for, onde pergunte qual tabuada o usuário deseja visualizar.
"""
tabuada = int(input('Escolha a tabuada que deseja visualizar: '))

print('{} {}'.format('TABUADA DO ', tabuada))
for n in range(1, 11):
    print('{} x {:2} = {:2}'.format(tabuada, n, (tabuada * n)))