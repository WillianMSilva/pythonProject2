peso = float(input('Insira seu peso: '))
altura = float(input('Insira sua altura:'))

imc = (peso)/(altura**2)

if imc <=18.5:
    print('Seu IMC {:.1f}. Você está abaixo do peso procure um médico'.format(imc))
elif imc <=24.9:
    print('Seu IMC {:.1f}. Você está com o peso normal, Parabénsss!!!'.format(imc))
elif imc <=29.9:
    print('Seu IMC {:.1f}. Você está com sobrepeso tome cuidado, procure orientação médica.'.format(imc))
elif imc <= 34.9:
    print('Seu IMC {:.1f}. Você está com Obesidade Grau I, procure um médico.'.format(imc))
elif imc <= 39.9:
    print('Seu IMC {:.1f}. Você está com Obesidade Grau II, procure um médico urgente.'.format(imc))
else:
    print('Seu IMC {:.1f}. Você está com Obesidade Grau III, procure urgentemente um hospital.'.format(imc))