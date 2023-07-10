#calcula seno, cosseno e tangente de um ângulo qualquer.

import math
ângulo = float(input('Digite o ângulo que você deseja: '))
seno = math.sin(math.radians(ângulo))
print('O ângulo {} tem o SENO de {:.2f} '.format(ângulo, seno))
cosseno = math.cos(math.radians(ângulo))
print('O ângulo {} tem o COSSENO de {:.2f}' .format(ângulo, cosseno))
tangente = math.tan(math.radians(ângulo))
print('O ângulo {} tem a TANGENTE de {:.2f}' .format(ângulo, tangente))
