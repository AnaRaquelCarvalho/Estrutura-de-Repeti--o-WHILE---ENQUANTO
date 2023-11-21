print('='*6, 'Jogo da Adivinhação com a Estrutura While ' , '='*6)
from random import randint
computador = randint(0, 10)
print('\n>>> Sou seu computador... Vou pensar em um número...')
print('>>> Acabei de pensar em um número de 0 a 10...\n')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Dê o seu palpite: '))
    palpites += 1
    if computador == jogador:
        acertou = True
    else:
        if jogador < computador:
            print('=' * 16, 'Mais...Tente mais uma vez. ', '=' * 16)
        elif jogador > computador:
            print('='*16,'Menos...Tente mais uma vez.','='*16)
print('='*46,'\nPARABÉNS! Acertou com {} tentavivas.'.format(palpites))
print('='*46)