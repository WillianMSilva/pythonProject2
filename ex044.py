#dinheiro/cheque 10%d desconto e cartão 5% desconto
#2 x preço normal, maior que 3x 20% de juros

valor = float(input('Insira o valor da compra: R$'))
print('formas de pagamento \n [1] à vista no dinheiro/cheque \n [2] à vista no cartão \n [3] 2x no cartão \n [4] 3x no cartão ou mais')
forma = int(input('Qual a opção para pagamento?'))

while forma >= 5:
    print('Código inválido tente novamente.')
    forma = int(input('Qual a opção para pagamento?'))
if forma == 1:
    print('Sua compra de R${} vai custar {} no final'.format(valor,(valor*90)/100))
elif forma ==2:
    print('Sua compra de R${} vai custar {} no final'.format(valor, (valor * 95) / 100))
elif forma ==3:
    print('Sua compra será parcelada em 2X de {} sem juros \nValor Parcelado {}'.format(valor/2,valor))
elif forma ==4:
    quantidade = int(input('Quantas parcelas?'))
    print('Sua compra será parcelada em {}x de {:.1f} com juros\nValor total parcelado {:.1f}'.format(quantidade,((valor*120)/100)/quantidade,(valor*120)/100) )

