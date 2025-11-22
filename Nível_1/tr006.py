numero1 = int(input('digiti um numero; '))
calculador = (input('vocé quer (+,-,*,/)'))
numero2 = int(input('digiti outro numero; '))
if calculador == '+':
    resu_calculo = numero1 + numero2
elif calculador == '-':
    resu_calculo = numero1 - numero2
elif calculador == '*':
    resu_calculo = numero1 * numero2
elif calculador == '/':
    resu_calculo = numero1 / numero2
else :
    print('VALOR INVALIDO')
print(f'{numero1}{calculador}{numero2}={resu_calculo}')