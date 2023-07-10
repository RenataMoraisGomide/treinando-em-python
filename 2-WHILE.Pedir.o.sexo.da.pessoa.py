# Faça um programa que leia o sexo da pessoa, mas só aceite os valores M/F.
# caso esteja errado, peça a digitação novamente até opter o correto.


sexo = str(input('Qual é o seu sexo [M/F]: ')).strip().upper() [0]
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos. Por favor informe o seu sexo: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso.'.format(sexo))

#OBS: aqui o while diz que enquanto o sexo não estiver dentro de Mm e Ff ele
#perguntará novamente qual é o sexo. Quando while for verdadeiro ele confirma o sexo