# Faça um jogo que o computador pense em um número de 0-10 e só pare quando o jogador acertar
# mostrando no final quantos palpites vc deu.

from random import randint
computador = randint(0, 10)
print('Vou pensar em um número entre 0 e 10, tente adivinhar...')
print('Consegue adivinhar qual foi? ')
acertou = False
palpite = 0
while not acertou:
    jogador = int(input('Qual o seu palpite? '))
    palpite += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais...tente novamente.')
        elif jogador > computador:
            print('Menos...tente novamente. ')
print('Acertou com {} palpites. '.format(palpite))
