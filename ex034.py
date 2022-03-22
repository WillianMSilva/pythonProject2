salario = float(input('Qual é o salário do funcionário?  R$ '))
if salario <= 1250:
#aumento de 15%
    print('Quem ganhava R${} passou a ganhar R${}'.format(salario,((salario*0.15)+salario)))
else:
#aumento de 10%
    print('QUem ganhava R${} passou a ganhar R${}'.format(salario,((salario*0.10))+salario))
