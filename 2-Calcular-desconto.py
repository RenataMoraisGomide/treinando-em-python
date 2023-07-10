# Elabore um programa que calcule o valor a ser pago por um produto, considerando
#o seu preço normal e condições de pagamento.
# a vista/cheque: 10% de desconto
# a vista cartão 5%
# em até 2 X no cartão: preço normal
# 3 X ou + 20% de juros


print('{:=^40}' .format(' Loja Artes Carmelitanas '))
preço = float(input('Qual o valor total: R$  '))
print(''' FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x cartão
[ 4 ] 3x ou mais cartão''')
opção = int(input('Qual a sua opção? '))
if opção == 1:
    total = preço - (preço * 10 / 100)
    print('O valor a vista é R$ {}'.format(total))
elif opção == 2:
    total = preço - (preço * 5 / 100)
    print('O valor a vista no cartão é: R$ {} '.format(total))
elif opção == 3:
    total = preço
    parcela = total / 2
    print('O valor em duas vezes de R$ {} no cartão e total de R$: {} '.format(parcela, total))
elif opção == 4:
    total = preço + (preço * 20 / 100)
    totparc = int(input('Quantas parcelas? '))
    parcela = total / totparc
    print('Sua compra será parcelada em {} X de R$ {:.2f}' .format(totparc, parcela))
    print('Sua compra de R$ {:.2f} vai custar R$ {:.2f} no final. '.format(preço, total))
else:
    print('Opção inválida')

print ('OBRIGADA!!!!!!')









