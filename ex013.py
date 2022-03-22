print('Calcule seu aumento de 15% no seu salário')
valor = float(input('Digite o valor do salário R$ '))
print('Seu salário com aumento de 15% é de R${:.2f} valor do seu novo salário'.format(((valor * 115) / 100) - valor),
      ((valor * 115) / 100))
