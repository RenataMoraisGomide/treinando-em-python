larg = float(input('Digite o valor da largura da parede: '))
alt = float(input('Digite a autura da parede: '))
area = larg * alt
print('Sua parede tem a dimensão de {} x {} e sua área é de {}m²'.format(larg, alt, area))
tinta = area / 2
print('Para pintar essa parede você irá precisar de {} litros de tinta' .format(tinta))
