# Crie um programa que calcule o IMC do usuário. 
# Revisão

print('*** C A L C U L A D O R A   I  M C ***\n')

peso = float(input('Digite seu peso (ex:72.5): '))
altura = float(input('\nDigite sua altura (ex: 1.80): '))

imc = peso / (altura * altura)

if imc < 18.5:
    print(f'\nSeu IMC é {imc:.2f}')
    print('Está abaixo do peso!')

elif imc < 24.9:
    print(f'\nSeu IMC é {imc:.2f}')
    print('Está com o peso normal, PERFEITO!') 

elif imc < 29.9:
    print(f'\nSeu IMC é {imc:.2f}')
    print('Está com sobrepeso!')

elif imc < 34.9:
    print(f'\nSeu IMC é {imc:.2f}')
    print('Está com obesidade grau I!')

elif imc < 39.9:
    print(f'\nSeu IMC é {imc:.2f}')
    print('Está com obesidade grau II!')

else:
    print(f'\nSeu IMC é {imc:.2f}')
    print('Está com obesidade grau III ou mórbida!')
    