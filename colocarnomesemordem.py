#colocar uma lista em ordem sorteada

import random
n1 = str(input('O primeiro nome: '))
n2 = str(input('O segundo nome: '))
n3 = str(input('O terceiro nome: '))
n4 = str(input('O quarto nome: '))
lista = [n1, n2, n3, n4]
random.shuffle(lista)
print('A ordem escolhida foi: ')
print(lista)

#aqui o random.shuffle (embaralhamento aleatório) escolhe uma ordem nos nomes.
#quando importamos a biblioteca random(embaralhar) tem várias opções de como embaralhar.
#pode importa no início a forma que quer embaralhar(no caso aqui shuffle, ficando:

from random import shuffle
n1 = str(input('O primeiro nome: '))
n2 = str(input('O segundo nome: '))
n3 = str(input('O terceiro nome: '))
n4 = str(input('O quarto nome: '))
lista = [n1, n2, n3, n4]
shuffle(lista)
print('A ordem escolhida foi: ')
print(lista)
