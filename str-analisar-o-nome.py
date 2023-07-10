n = str(input('Digite seu nome completo: ')).strip()
nome = n.split()
print('Muito prazer em te conhecer!')
print('Seu primeiro nome é: {} ' .format(nome[0]))
print('Seu último nome é: {}' .format(nome[len(nome)-1]))

#Nesse exercício entramos com .strip() eliminando espaçamento no início e fim
#na linha 2 o nome = n.split() significa que o nome será separado 'Ana' 'Maria'... na posicão de (0 e 1...)
#Na 4° seleciona apenas o primeiro nome tendo ele a posição 0 .format(nome[0])
#na 5° seleciona o último -1 para que conte todos (pois inicia no 0)
