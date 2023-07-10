# Crie um programa que jogo JOKENPÔ com você
# Pedra/papel/tesoura

from random import randint
from time import sleep

itens = ('pedra', 'papel', 'tesoura')
computador = randint(0, 2)
print('''Suas opções
[ 0 ]pedra
[ 1 ]papel
[ 2 ]tesoura ''')
jogador = int(input('Qual é a sua jogada? '))
print('JO')
sleep (1)
print('KEN')
sleep(1)
print('PO!!!!!')
sleep(1)
print('-=' *12)
print('O computador jogou {}' .format(itens[computador]))
print('Jogador jogou: {} '.format(itens[jogador]))
print('-=' *12)

if computador == 0:
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('Jogador Vence!!!')
    elif jogador == 2:
        print('Computador Vence!!')
    else:
        print('Jogada inválida!')

if computador == 1:
    if jogador == 0:
        print('Computador Vence!!!')
    elif jogador == 1:
        print('Empate')
    elif jogador == 2:
        print('Jogador vence!!!')
    else:
         print('Jogada inválida!')

elif computador == 2:
    if jogador == 0:
        print('Jogador vence!!!')
    elif jogador == 1:
        print('Computador vence!!!')
    elif jogador == 2:
        print('Empate')
    else:
        print('Jogada inválida!')
















