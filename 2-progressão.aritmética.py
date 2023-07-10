# Desenvolva um programa que leia o primeiro terno e a razão de uma PA. No final, mostre os 10 primeiros
# termos dessa progressão.

print('==' * 10)
print('10 termos de uma PA')
print('==' * 10)

primeiro = int(input('Qual o primeiro termo? '))
razão = int(input('Qual a razão? '))
décimo = primeiro + (10 - 1) * razão
for c in range(primeiro, décimo + razão, razão):
    print('{}' .format(c), end= ' -> ')
print('ACABOU!')
