viagem = float(input('Qual é a distância da sua viagem em KM: '))
if viagem <=200:
    print('O valor cobrado é {}'.format(viagem*0.50))
else:
    print('O valor cobrado é {}'.format(viagem*0.45))
