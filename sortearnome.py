#Sortear um nome lendo alguns e escrevendo o nome do escolhido

import random
n1 = str(input('Primeiro nome: '))
n2 = str(input('O segundo nome: '))
n3 = str(input('O terceiro nome: '))
n4 = str(input('O quarto nome: '))
lista = [n1, n2, n3, n4]
escolhido = random.choice(lista)
print('O aluno escolhido foi: {} '.format(escolhido))

#random choice (o computador) escolhe um da lista
