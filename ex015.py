print('Sabia qual o valor do aluguel do seu carro')
dias = int(input('Digite a quantidade de dias: '))
km = float(input('Digite a quantidade de km: '))
#.format inserir dentro as operações matemáticas
print ('Valor total do seu alguel é R${:.2f}'.format((dias*60)+(km*0.15)))