casa = float(input('Digite o valor da casa R$ '))
salario = float(input('Digite o valor do seu salário R$ '))
anos = float(input('Digite a quantidade de anos: '))
limite = salario*0.3
meses = anos*12
parcela = casa/meses
if parcela < limite:
    print('Se o valor da casa for {} o valor da parcela será de R${:.2f} por mês \n FINANCIAMENTO CONCEDIDO'.format(casa,parcela))
else:
    print('Para pagar um financiamento de {} em {} anos a parcela será de R${:.2f}. \n FINANCIAMENTO NEGADO'.format(casa,anos,parcela))
