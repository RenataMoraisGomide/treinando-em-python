# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu índice de Massa
# corporal (IMC) e mostre seu status, de acordo com a tabela:
#IMC abaixo de 18.5: abaixo do peso
#IMC entre 18.5 e 25: peso ideal
#25 a 30 : Sobrepeso
#30 a 40: obesidade
# IMC = peso / altura ²

peso = float(input('Qual o peso? kg '))
altura = float(input('Qual a sua altura? '))
IMC = peso / altura ** 2
print('Seu IMC é {}.'.format(IMC))
if IMC < 18.5:
    print('Você está abaixo do peso.')
elif IMC > 18.5 and IMC < 25:
    print('Seu peso esta ideal para sua altura.')
elif IMC > 25 and IMC < 30:
    print('Você está com sobrepeso.')
elif IMC > 30 and IMC < 40:
    print(' Você está com obesidade.')
else:
    print('Obesidade mórbida!')
