#condições simples, compostas e simplificadas.
#Montar um programa onde ele irá ler a velocidade de um carro. Se ele ultrapassar a velocidade de 80km/h, mostrar
#uma mensagem dizendo que ele foi multado.
#calcular a multa que custará R$7,00 por km acima do limete.

velocidade = (float(input('Qual a velocidade em km/h: ')))
if velocidade > 80:
    print('MULTADO!!! Você excedeu o limite que é 80 km/h')
    multa = (velocidade - 80)*7
    print('Você irá pagar uma multa de R$: {:.2f}! '.format(multa))
print('Tenha um bom dia! Dirija com segurança!')
