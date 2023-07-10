# Escreva um programa que leia um número inteiro qualquer e peça ao usuário que escolha qual a base sera
# feita a conversão: 1 para binário, 2 para octal e 3 para hexadecimal

num = int(input('Digite um número inteiro: '))
print('''Escola a base para conversão:
[ 1 ]Converter para binário
[ 2 ]Converter para octal
[ 3 ]Converter para hexadecima''')
opção = int(input('Sua opção: '))
if opção == 1:
    print('{} convertido para binário é igual a {} .' .format(num, bin(num)[2:]))
elif opção == 2:
    print('{} convertido para octal é igual a {}. ' .format(num, oct(num)[2:]))
elif opção == 3:
    print('{} convertido para Hexadecimal é igual a {}.' .format(num, hex(num)[2:93]))
else:
    print('Opção inválida. Tente novamente!')