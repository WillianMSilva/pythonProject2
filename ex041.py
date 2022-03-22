from datetime import date
nasc = int(input('Ano de Nascimento: '))
#Date.today.year para pegar a data do dia do sistema
data = date.today().year
idade = data - nasc

#ate 9 anos mirim
#ate 14 infatil
#ate 19 junior
#ate 25 senior
#acima master

if idade <= 9:
    print('O atleta tem {} anos \n Classificação: MIRIM.'.format(idade))
elif idade <= 14:
    print('O atleta tem {} anos \n Classificação: INFANTIL'.format(idade))
elif idade <= 19:
    print('O atleta tem {} anos \n Classifcação: JUNIOR'.format(idade))
elif idade <= 25:
    print(('O atleta tem {} anos \n Classificação: Sênior'.format(idade)))
else:
    print('O atleta tem {} anos \n Classificação: MASTER'.format(idade))


