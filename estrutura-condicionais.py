#aqui falaremos das estruturas condicionais: V ou F e apenas 1 será executado.
#Condição simples if e composta if/else: (#SE #SENÃo)
#   ifcarro.esquerda(): bloco True   / else: bloco False
#EX:

tempo = int(input('Quantos anos tem seu carro?'))
if tempo<=3:
    print('carro novo')
else:
    print('carro velho')
print('---fim---')

nome = str(input('Qual é o seu nome?'))
if nome == 'Renata':
    print('Que nome lindo você tem!')
else:
    print('Que nome normal!')
print('Bom dia {}' .format(nome))


n1 = float(input('Qual a primeira nota: '))
n2 = float(input('Qual a segunda nota: '))
m = (n1+n2)/2
print('A sua média foi: {} '.format(m))
if m >= 6:
    print('Sua média foi boa')
else:
    print('Que nota horrível')
