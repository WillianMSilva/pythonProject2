#importação da biblioteca datetime a função data
from datetime import date
ano = int(input(' Que ano quer analisar? Coloque 0 para analisar o ano atual: '))
#Essa função para o programa pegar a data do ano correspondente da máquina
if ano == 0:
    ano = date.today().year
#Para ano bisexto não é somente o divisivel por 4 segue fórmula abaixo
if ano % 4 == 0 and ano % 100 or ano % 400 == 0:
    print('ano {} é bisexto'.format(ano))
else:
    print('ano {} não é bisexto'.format(ano))
