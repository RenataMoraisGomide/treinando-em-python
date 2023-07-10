# Crie um programa que leia uma frase e diga se ela é um palíndromo (frases que lidas em qualque sentido
# tem as mesmas palavras), desconsiderando os espaços.


frase = str(input('Digite uma frase: ')).strip().upper()     #li a frase eliminando espaços e fazendo ficar toda maiúscula
palavras = frase.split()                                     #split para que gere um vetor(uma lista)
junto = ''.join(palavras)                                    #juntou tudo em uma str só
inverso = ''                                                 #mandei inverter
for letra in range(len(junto) - 1, -1, -1):                  #usei o for para inverter e ir da última letra voltando para a primeira
    inverso += junto[letra]
print('O inverso de {} é {}'.format(junto, inverso))         #olhar se o inverso é =
if inverso == junto:
    print('Temos um palíndromo!')
else:
   print('Não tempos um palíndromo!')