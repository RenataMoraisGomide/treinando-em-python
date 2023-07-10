# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade
# se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se passou do tempo
# O programa também deverá mostrar o tempo que falta ou o que passou.


from datetime import date
atual = date.today().year

sexo = str(input('Qual seu sexo: '))
nasc = int(input('Ano de nascimento: '))
idade = (2023 - nasc)
passou = idade - 18

if sexo == 'feminino':
    print('Você não precisa se alistar no serviço militar.')
elif sexo == 'masculino':
    print('Você precisa alistar no serviço militar. Vamos analisar quando?')
    print('Quem nasceu em {} tem {} em {}.'.format (nasc, idade, atual))
if idade < 18:
    print('Você ainda deve se alistar no serviço militar')
elif idade > 18 and sexo == 'masculino':
    print('Você passou do prazo em {} anos de se alistar.'.format (passou))
elif idade == 18:
    print('Você tem que se alistar imediatamente.')



