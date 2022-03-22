numero = int(input('Me diga um número qualquer: '))
# fazer o resto da divisão por 2, sempre que for 1 será números impares e 0 para os pares.
resultado = numero % 2
#print('o resultado foi {}'.format(resultado))
if resultado == 0:
    print('O número {} é par'.format(numero))
else:
    print('O numéro {} é ímpar'.format(numero))