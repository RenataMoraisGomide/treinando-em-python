real = float(input('Quanto de dinheiro você tem na carteira? R$ '))
dolar = real / 4.99
print('Com R$ {} você pode comprar US$ {:.2f}'.format(real, dolar))
euro = real / 5.55
print('Com R$ {} você pode comprar £ {:.2f}'.format(real, euro))
