#Faça um programa que leia três números e mostre qual deles é o maior e qual é o menor

a = int(input('Digite um valor: '))
b = int(input('Digite outro valor: '))
c = int(input('Digite mais um valor: '))

#pode fazer assim:
#verificando quem é o menor:
if a < b and a < c:
    menor = a
if b < c and b < a:
    menor = b
if c < a and c < b:
    menor = c

print('O menor valor digitado foi: {}'.format(menor))

#verificando quem é o maior:

if a > b and a > c:
    maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c

print('O maior valor digitado foi: {}'.format(maior))
