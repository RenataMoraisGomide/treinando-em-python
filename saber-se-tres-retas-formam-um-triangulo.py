#crie um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não
#formar um triângulo.
#equilátero(todos os lados tem que ser iguais)
#isósceles(dois lados iguais e um diferente)
#escaleno(todos os lados diferentes)


print('-=-'*8)
print('Analisador de triângulos')
print('-=-'*8)


r1 = float(input('Qual o valor da reta 1? '))
r2 = float(input('Qual o valor da reta 2? '))
r3 = float(input('Qual o valor da reta 3? '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima pode formar um triângulo.')
    if r1 == r2 == r3:
        print('Triângulo EQUILÁTERO')
    elif r1 != r2 != r3 != r3 != r1:
        print('Triângulo ESCALENO')
    else:
        print('Triângulo ISÓSCELES')
else:
    print('Os segmentos acima não podem formar um triângulo.')
