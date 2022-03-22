dinheiro = float(input('Conversor Reais em Doláres \n Insira o Valor:R$ '))
conversor = dinheiro / 3.27

if conversor < 1:
    print('R${} reais é igual a US${:.2f} centavos'.format(dinheiro, conversor))
else:
    print('R${} reais é igual a US${:.2f} doláres'.format(dinheiro, conversor))
