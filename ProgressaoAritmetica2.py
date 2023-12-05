print('='*8, 'Prograssão Aritmética - PA','='*8)
print('   >>>>>>>>>  Gerador de PA   <<<<<<<<<<  ')
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
print('='*60)
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} '.format(termo),end='➞ ')
        termo += razao
        cont += 1
    print('Pausa!!!')
    mais = int(input('Quantos termos você quer mostrar a mais: '))
    print('=' * 60)
print('Progressão finalizada com {} termos mostrados.'.format(total))
print('='*60)