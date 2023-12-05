print('-'*36)
print('     Tratando vários valores     ')
print('-'*36)
n = cont = soma = 0    #TODAS AS VARIÁVEIS RECEBEM O NÚMERO ZERO.
n = int(input('Digite um número [999 para PARAR]: '))
while n != 999:
    soma += n
    cont += 1
    n = int(input('Digite um número [999 para PARAR]: '))
print('-'*36)
print('Você digitou {} números e a SOMA entre eles foi {}'.format(cont, soma))
print('-'*36)