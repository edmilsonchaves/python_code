#_______________________________FUNÇÕES DE ESTILIZAÇÃO E INICIALIZAÇÃO________________________________

def branco(texto):
    print(f'\033[30m{texto}\033[m')

def vermelho(texto):
    print(f'\033[31m{texto}\033[m')

def verde(texto):
    print(f'\033[32m{texto}\033[m')

def amarelo(texto):
    print(f'\033[33m{texto}\033[m')

def azul(texto):
    print(f'\033[34m{texto}\033[m')

def roxo(texto):
    print(f'\033[35m{texto}\033[m')

def azul_claro(texto):
    print(f'\033[36m{texto}\033[m')

def cinza(texto):
    print(f'\033[37m{texto}\033[m')

def tracejado():
    azul_claro('=' * 40)

def apresentacao():
    tracejado()
    azul('{:=^40}'.format(' TABUADA 2.0 '))
    tracejado()
