número = int(input('Diga um número qualquer: '))
resultado = número % 2
if resultado == 0:
    print('O número {} é par.'.format (número))
else:
    print('O número {} é ímpar.'.format(número))