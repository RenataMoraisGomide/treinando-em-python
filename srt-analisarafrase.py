#faça um programa que leia uma frase pelo teclado e mostre:
#quantas vezes aparece a letra A
#em que posição ela aparece primeiro e qual a última.


frase = str(input('Digite uma frase: ')).upper().strip()
print('A letra A aparece {} vezes nessa frase.'.format(frase.count('A')))
print('A primeira letra A apareceu na posição {} '.format(frase.find('A')+1))
print('A última letra A apareceu na posição{}'.format(frase.rfind('A')+1))

#OBS: na linha 6 quando colacamos .upper() fazemos com que automaticamente o computador jogue todas as letras
#A maiúsculas para que não gere erro. Quando usamos o .strip() ele deleta automaticamente os espaços do início e fim.
#Na linha 7 vamos contar quantos A aparece usando o .format(frase.find('A')+1)) esse +1 é apenas para fazer a contagem
#como nós pois o computador irá iniciar em 0 e não em 1, Então Renata ficaria com o 1° A na posição 3 e não na 4°
