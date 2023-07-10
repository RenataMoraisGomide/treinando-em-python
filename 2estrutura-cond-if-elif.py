#MUNDO 2
#ESTRUTUTA DE CONTROLE
#condições aninhadas é colocar uma condição dentro de outra (ninho)
# if(se)  elif (senão se)  else (se não)
#dentro do if pode usar vários elif

nome = str(input('Qual é o seu nome? '))
if nome == 'Renata':
    print ('Que nome bonito!')
elif nome=='Pedro' or nome == 'Maria' or nome == 'José':
    print('Seu nome é comum no Brasil.')
elif nome in 'Ana Cláudia Lara':
    print('Belo nome feminino')
else:
    print('Seu nome é bem normal {}'.format(nome))

print('Tenha um bom dia {} !'.format(nome))