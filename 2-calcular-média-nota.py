#n1 = float(input('A primeira nota do aluno: '))
#n2 = float(input('A segunda nota do aluno: '))
#m = n1+n2
#mt = m/2
#print('O valor da média entre {}, {} é igual a {} '.format(n1, n2, mt))

#pode usar também m=(n1+n2)/2 assim os () serão resolvidos primeiro.

n1 = float(input('Qual a primeira nota: '))
n2 = float(input('Qual a segunda nota: '))
m = (n1 + n2) / 2
print('Calculando as suas notas {} e {}, temos a média {} '.format(n1, n2, m))
if m < 5:
    print('VOCÊ FOI REPROVADO')
elif m >= 5 and m < 6.9:
    print('VOCÊ ESTÁ DE RECUPERAÇÃO')
else:
    print('PARABÉNS!!! VOCÊ FOI APROVADO!!!')
