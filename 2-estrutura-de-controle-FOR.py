# Repetir as coisas,  aqui vamos aprender a fazer e usar a estrututa de controle FOR
# laços, repetições e iteração
# laço de variável de controle
# ex: laço c no intervalo(1,10)
#   passo
#pega
#        for c in range(1,10): (irá seguir e repetir o comando)

# ex: laço c no intervalo(0,3)
#   passo/pula
#   passo pega
#       for c in range(0,3):  (irá dar passo/pula 3 vezes)



for c in range(1,10):
    print('OI')
print('FIM')

#Aqui ele vai contar até 9 (não entra o 10) e no "print" (c) é sem aspas se não ele copia ccccccccc
for c in range(1, 10):
    print(c)
print('FIM')

#Aqui ele vai contar de 6 a 1 (esse -1 do código faz ele contar diminuindo 1)
for c in range(6, 0, -1):
    print(c)
print('FIM')

#Aqui ele vai contar de 0 a 8 ( de 2 em 2)
for c in range(0, 10, 2):
    print(c)
print('FIM')

#Aqui vai ler um número e no comando for ele vai contar de 0 até o número dado. ( o +1 é para que ele conte de 0 até o número
# se não colocar ele conta até o anterior.
n = int(input('Digite um número: '))
for c in range(0, n + 1):
    print(c)
print('Fim')


#Aqui lemos 3 passos ( i, f, p) f=o for fez ele inicar a repetição em i, passou para f+1, e p: pulando de ....
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i, f+1, p):
    print(c)
print('Fim')


# Aqui entramos s = 0 a repetição pedirá 4 valores e depois somará (s += n) s+n
s = 0
for c in range(0,4):
    n = int(input('Valor: '))
    s += n
print('a soma dos valores foi: {}'.format(s))




