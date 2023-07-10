# Faça um programa que leia 5 pesos e diga qual o maior lido e o menor




maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input('Qual o peso da {}ª pessoa? '.format(p)))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso lido foi {} kg '.format(maior))
print('O menor peso lido foi {} kg '.format(menor))