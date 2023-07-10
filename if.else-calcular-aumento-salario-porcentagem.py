#calcular porcentagem
#escreva um programa que leia um salário e calcule seu aumeto onde será 10% para salários acima de 1.250,00
#e 15% para salários menores.

salário = float(input('Qual o salário do funcionário? R$ '))
if salário <= 1250:
    novo = salário + (salário * 15 / 100)
else:
    novo = salário + (salário * 10 / 100)

print('Quam ganhava:R$ {:.2f} passa a ganhar R${:.2f} agora. '.format(salário, novo))

