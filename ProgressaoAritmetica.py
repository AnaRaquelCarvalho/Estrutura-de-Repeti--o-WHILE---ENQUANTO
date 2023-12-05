print('='*8, 'Prograssão Aritmética - PA','='*8)
print('   >>>>>>>>>  Gerador de PA   <<<<<<<<<<  ')
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
print('='*60)
termo = primeiro
cont = 1
while cont <= 10:
    print('{} '.format(termo),end='➞ ')
    termo += razao
    cont += 1
print('Acabou!!!')
print('='*60)