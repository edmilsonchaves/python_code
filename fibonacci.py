# Sequência de Fibonacci
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597,

n1 = 0
n2 = 1
i = 0
print('{:^30}'.format('SEQUÊNCIA DE FIBONACCI'))
qtd = int(input("Quantas sequência de Fibonacci: "))

print(f'{n1} → {n2} → ',end='')
while i <= qtd:
    n3 = n1 + n2
    print(f'{n3} → ',end='')
    n1 = n2
    n2 = n3
    i += 1
print('FIM')
