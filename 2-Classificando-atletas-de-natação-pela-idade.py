# A confederação Nacional de Natação precisa de um programa que leia o ano de nascimento
# de um atleta e mostre sua categoria de acordo com a idade:
# *até 9 anos - mirim
# *até 14 ANOS - infantil
# *até 25 anos - Sênior
# *acima de 25 anos - Master

from datetime import date
atual = date.today().year

nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
if idade <= 9:
    print('Você tem {} anos e está na categoria MIRIM. '.format(idade))
elif idade >=10 and idade <= 14:
    print('Você tem {} anos e está na categoria INFANTIL. '.format(idade))
elif idade > 14 and idade <= 25:
    print('Você tem {} anos e está na categoria SÊNIOR. '.format(idade))
else:
    print('Você tem {} anos e está na categoria MASTER. '.format(idade))

