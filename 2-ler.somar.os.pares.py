# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que foram par.
# se o valor digitado for ímpar desconsidere.


soma = 0
cont = 0
for c in range(1,7):
    num = int(input('Qual o {}° valor: '.format(c)))
    if num % 2 == 0:
        soma += num
        cont = cont + 1
print('Você informou {} números pares e a soma foi {} '.format(cont, soma))
