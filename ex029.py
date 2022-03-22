velocidade = float(input('Qual a sua velocidade? '))

if velocidade<=80:
    print('Tenha um bom dia! Dirija com segurança.')
else:
    print('Você ultrapassou a velocidade em {} km/h a sua multa será {:.2f}'.format(velocidade-80, (velocidade-80)*7))
