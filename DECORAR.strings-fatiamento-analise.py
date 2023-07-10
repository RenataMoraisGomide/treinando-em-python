#fatiamento:
#cadeia de caracteres ou strings (cordas) onde cada caracter chama índice (contado espaço)
#cada caracter é separado onde podemos fazer o fatiamento ex: frase[9:13](ele vai pergar aqui no caso do
#caracter 9 até o 12(não entra o último valor na contagem)
#se usar ex: [9:21:2] ele irá pegar do 9 ao 20 pulando de 2 em 2
#se usar ex [:5] quando não coloca o primeiro-onde começar ele pega do início (0) até onde está mandando.
#se usar ex:[15:] quando não define o fim ele pegará até o último número.
#se [9::3] vai começar onde manda e vai até o final indo (no caso de 3 em 3.

#análise:
#len = comprimento ( se mandar mostrar o len da frase ele mostraria quantos micro-espaços ela tem.
#count = ele conta quantas vezes uma certa letra aparecerá na frase. ex:frase.count('o')
#se colocarmos frase.count('o',0,13) ele te daria quantas letras O aparecem até o intervalo do 13 caracter da frase
#find = encontrar ex: frase.find('deo'), isso mostraria onde se encontra o início de DEO quando aparece na frase
#se receber a função -1 é quando a str não foi encontrado

#transformação:
#replace = substituir ex: frase.replace('Python', 'android'), aqui ele vai achar a palavra python e trocar pela
#palavra android.
#upper é um método e precisa colocar depois dele () =significa superior/pra cima/maiusculas =
#frase.upper() ele trará todas as letras em maiúsculas.
#lower = mais baixo, minúsculas. Ele é o contrário do upper, faz com que a frase venha em minúsculas.
#também é um método então fica: frase.lower()
#capitalize = capitalizar = é um método então usa () após ficando: frase.capitalize()
#ele faz com que apenas a primeira letra da frase fique maiúscula e as demais fiquem minúsculas.
#title = título = também é um método ex: frase.title() e ele fará com que todas as primeiras letras das palavras da
#frase fiquem em maiúsculo.
#strip = faixa = remove todos os espaços desnecessários no começo e final da frase/str. frase.strip()
#rstrip = R de right (direita) ele é método ficando frase.rstrip(), serve para remover apenas os espaços da direita.
#lstrip = L de left (esquerda) ele remove o espaço desnecessário da esqueda. frase.lstrip()

#DIVISÃO:
#split = dividir = pega a str e dividir separando as células onde cada palavra ficará separada (gera outra lista)
#sem espaço e sua contagem recomeça do 0 novamente. frase.split()

#JUNÇÃO:
# '-'.join(frase) _ ele separa a str cada palavra separada por - ex: Renata-Morais
#o join pode usar ' ' espaço e ele ficará apenas com espaço entre os nomes.

















