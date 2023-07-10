#Aula de como trabalhar com cores no terminal
#Aula 20
# #código ANSI \
# ex: \033[style; text; back m
#códigos para estilo: 0 (sem estilo), 1(negrito), 4(sublinhado/underline) e 7 (negative/invertido)
#códigos para cores(text): 30(branco), 31(vermelho), 32(verde), 33(amarelo), 34(azul), 35(lilas), 36 (verde agua), 37(cinza)
#códigos de fundos(back): 40, 41, 42, 43, 44, 45, 46, 47 (usando as cores acima)

print(' \033[0;30;41mOlá Mundo! \033[m')
print(' \033[1;31;44mOlá Mundo! \033[m')
print(' \033[4;30;45mOlá Mundo! \033[m')
print(' \033[7;30;45mOlá Mundo! \033[m')
print(' \033[7;33;44mOlá Mundo! \033[m')

