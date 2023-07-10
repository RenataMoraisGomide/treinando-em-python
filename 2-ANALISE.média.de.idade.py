# Desenvolva um programa que leia o nome, idade e o sexo de 4 pessoas. No final ele mostra: a média da idade do grupo
# qual é o nome do mais velho e quantas mulheres têm menos de 20 anos.

somaidade = 0
médiaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0
for p in range(1, 5):
    print('-----{}ª PESSOA -----' .format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('idade: '))
    sexo = str(input('sexo [M/F]: ')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1
médiaidade = somaidade / 4
print('A média de idade do grupo é de {} anos. '.format(médiaidade))
print('O homem mais velho tem {} anos e se chama {}' .format(maioridadehomem, nomevelho))
print('Ao todo são {} mulher (es) com menos de 20 anos. '.format(totmulher20))