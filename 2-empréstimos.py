# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor
# da casa, o salário do comprador e em quantos anos ele irá pagar. A prestação mensal não pode exceder
# 30% do salário ou então o empréstimo será negado.

casa = float(input('Qual o valor total da casa?R$ '))
anos = int(input('Quantos anos de financiamento? '))
salário = float(input('Qual o salário do comprador?R$ '))
prestação = casa / (anos * 12)
mínimo = salário * 30 / 100
print ('Para pagar uma casa de R$ {:.2f} em {} anos, a prestação será de R${:.2f}' .format (casa,anos,prestação) )
if prestação <= mínimo:
    print('Empréstimo pode ser concedido!')
else:
    print('O empréstimo não pode ser concedido')
print('Comparando tem que pagar {} e o mínimo é {}.' .format(prestação, mínimo))



