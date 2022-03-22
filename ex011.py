print('Calcule quantos litros você precisa para pintar uma parede')
altura = float(input('Digite a altura em metros: '))
largura = float(input('Digite a Largura em metros: '))

metros = altura * largura
litros = (metros * 1)/2

if litros <1:
    print (' Você precisa de {:.1f} ml para pintar sua parede'.format((litros*1000)))
else:
    print ('Você precisa de {} litros de tinta para pintar sua parede'. format(litros))
