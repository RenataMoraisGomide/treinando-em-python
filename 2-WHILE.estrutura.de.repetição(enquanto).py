#Usada quando não sabemos quantas repetições precisamos. Não sabemos o limite
# WHILE é uma estrutura de repetição com teste lógico e o FOR é Estrutura de repetição com variável de controle.

'''for c in range(1, 10):       #FOR se souber o limite
    print(c)
print('FIM')'''

'''c = 1                           #o contador começa no 1
while c < 10:                   #enquanto o contador for menor que 10 (ou não for 10)
    print(c)
c = c + 1                       #c será c + 1
print('FIM')'''


n = 1                                           #aqui colocamos que ele irá perguntas 'DIGITE UM VALOR' até que
while n != 0:                                   #o valor dado seja 0, caso não coloque 0 ele ficará repetindo.
    n = int(input('Digite um valor: '))
print('FIM!!!')



