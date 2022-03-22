import random
print('Vamos jogar!! \n Pensei em um número de 1 a 5')
numero = int(input('Qual foi o número que pensei? Digite o número '))

lista = [0,1,2,3,4,5]
ram = random.choice(lista)

if ram == numero:
    print('acertouuu')
else:
    print('Errouuu o número foi {} '.format(ram))
