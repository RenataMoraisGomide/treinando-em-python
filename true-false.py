cid = str(input('Em que cidade você nasceu? ')).strip()
print(cid[:5].upper() == 'SANTO')



### O .strip() elimina os espaços no início e no fim
# Quando usei o .upper() == 'SANTO' ele fará com que a palavra se torne toda maiúscula não dando margem a erro
# quando digitado em maiúsculas e minúsculas.
#Santo/santo/SanTo será lido apenas SANTO


nome = str(input('Qual é o seu nome? ')).strip()
print('Seu nome tem Silva? {} '.format('SILVA' in nome.upper()))
