num = int(input('Informe um número: '))
n = str(num)
print('Analisando o número {} .' .format(num))
print('unidade {}'.format(n[3]))
print('dezena: {}'.format(n[2]))
print('centena: {}'.format(n[1]))
print('milhar: {}'.format(n[0]))

#nesse exemplo acima quando executar e o número tiver menos que 4 digitos não dará certo então resolve-se assim:
#usando % ele pega o resto

num = int(input('Informe um número: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Analisando o número {} .' .format(num))
print('unidade {}'.format(u))
print('dezena: {}'.format(d))
print('centena: {}'.format(c))
print('milhar: {}'.format(m))