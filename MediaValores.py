print('-'*36)
print('     MAIOR, MENOR E MÉDIA VALORES')
print('-'*36)
Resp = 'S'
soma = cont = media = maior = menor = 0
while Resp in 'Ss':
    num = int(input('Digite um número: '))
    soma += num
    cont += 1
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
            if num < menor:
                menor = num

    Resp = str(input('Quer continuar? [S/N]: ')).upper().strip()
    media = (soma / cont)
print('-'*64)
print('Você digitou {} números e a MÉDIA entre eles foi {:.2f}'.format(cont, media))
print('O Maior número foi {} e o MENOR número foi {}.'.format(maior,menor))
print('ACABOU!!!')
print('-'*64)

