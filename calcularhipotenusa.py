co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = (co ** 2 + ca **2) ** (1/2)
print('A hipotenusa vai medir: {:.2f}' .format(hi))

#hipotenusa é igual a soma dos quadrados dos catetos.

import math
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = math.hypot(co, ca)
print('A hipotenusa vai medir: {:.2f}' .format(hi))

#aqui usamos a importação de math.hypot (que calcula direto a hipotenusa)
