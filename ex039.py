#importar a biblioteca de data
from datetime import date

ano = int(input('Ano de nascimento: ' ))
#sexo = str(input('Qual sexo F / M: '))

#contabilizar a data do sistema do computador
date = date.today().year

idade = date-ano
alist = ano+18
#if sexo == M:

    #print('Você não precisa fazer o serviço militar')
if idade < 18:
    print('Quem nasceu em {} tem {} em {}'.format(ano,idade,date))
    print('Ainda faltam {} para o alistamento'.format(18-idade))
    print('Seu alistamento será em {}'.format(alist))
elif idade > 18:
    print ('Quem nasceu em {} tem {} em {}'.format(ano,idade,date))
    print('Ja se passaram {} anos do alistamento'.format(idade-18))
    print('Seu alistamento foi em {}'.format(alist))
else:
    print('Quem nasceu em {} tem {} em {}'.format(ano,idade,date))
    print('Você tem que se alistar IMEDIATAMENTE')



