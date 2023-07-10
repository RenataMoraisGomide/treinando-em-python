# Escreva um programa que leia dois números inteiros e compare-os mostrando qual o maior e qual o menor

num1 = int(input('Digite um valor inteiro: '))
num2 = int(input('Digito o outro valor inteiro: '))
if num1 > num2:
    print('O primeiro valor é maior.')
elif num1 < num2:
    print('O segundo valor é maior. ')
elif num1 == num2: #aqui pode usar só o else
    print('Não existe valor maior, os dois são iguais.')
