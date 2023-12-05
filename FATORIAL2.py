print('='*3,'Calculo do Fatorial - Estrutura While (Enquanto)','='*3)
n = int(input('Digite um número para calcular o Fatorial: '))
c = n
f = 1
print('>>>>>> Calculando o Fatorial de {} <<<<<<\n'.format(n), end='')
while c > 0:
    print('{}'.format(c), end=' ')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))
print('='*56)