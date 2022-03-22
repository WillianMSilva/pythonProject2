n1 = float(input('Primeira Nota: '))
n2 = float(input('Segunda Nota: '))

nota = (n1+n2)/2

if nota >= 7.0:
    print('Sua média foi {}, você está APROVADO'.format(nota))
elif nota >= 5 < 7:
    print('Sua média foi {}, você está de RECUPERAÇÃO'.format(nota))
elif nota < 5.0:
    print('Sua média foi {}, você está RERPOVADO'.format(nota))
