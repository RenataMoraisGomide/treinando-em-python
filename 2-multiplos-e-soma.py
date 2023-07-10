# Faça um programa que calcule a soma entre todos os números múltiplos de três
# no intervalo de 1 até 500 e some eles.


s = 0
cont = 0
for c in range(0, 501, 3):
   print(c, end='  ')
   cont = cont + 1
   s += c
print('A soma de todos os {} número de três em três é: {} '.format(cont, s))


