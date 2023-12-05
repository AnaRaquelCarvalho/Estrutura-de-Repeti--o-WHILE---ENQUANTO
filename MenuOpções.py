print('='*6, 'Criando um Menu de opções' ,'='*6)
from time import sleep
n1 = int(input('Informe o 1º valor: '))
n2 = int(input('Informe o 2º valor:  '))
opcao = 0
while opcao != 5:
    print('>> Escolha uma das opções abaixo: <<')
    print('''       [1] SOMAR
       [2] MULTIPLICAR
       [3] MAIOR VALOR
       [4] NOVOS NÚMEROS
       [5] SAIR DO PROGRAMA''')
    opcao = int(input('Qual a sua opção: '))
    if opcao == 1:
        print('A SOMA entre {} + {} = {}'.format(n1, n2, n1 + n2))
    elif opcao == 2:
        print('A MULTIPLICAÇÃO entre {} x {} = {}'.format(n1, n2, n1 * n2))
    elif opcao == 3:
        if n1 > n2:
            maior = n1
            print('O MAIOR VALOR digitado foi {}'.format(maior))
        elif n2 > n1:
            maior = n2
            print('O MAIOR VALOR digitado foi {}'.format(maior))
    elif opcao == 4:
        print('=-=' * 16)
        print('Informe os números novamente.')
        n1 = int(input('Informe o 1º valor: '))
        n2 = int(input('Informe o 2º valor:  '))
    elif opcao == 5:
        print('FINALIZANDO...')
    else:
        print('Opção Inválida! Tente novamente!')
    print('=-=' * 16)
    sleep(3)
print('Fim do Programa! Volte Sempre!')
print('=-=' * 16)