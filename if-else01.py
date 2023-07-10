#Faça um jogo que o computador escolhe um número de 1 a 5 e você tenta adivinhar qual é esse
#número, se acertar ele te dará parabéns e se errar ele diz que errou.

from random import randint   #aqui importamos a bibliotaca random e usamos randint(que gera um número int. em um intervalo)
computador = randint(0, 5)  #faz o computador "PENSAR O NÚMERO"
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5, tente adivinhar...')
print('-=-' *20)
jogador = int(input('Em que número pensei?'))     #Aqui o jogador tenta adivinhar
if jogador == computador:
    print('Parabéns você ganhou!!!')
else:
    print('Ganhei! Eu pensei no número {}, e não no número {}' .format(computador, jogador))
