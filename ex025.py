#sempre usar .strip para tirar os espaços excedentes
nome = str(input('Qual é o seu nome completo? ')).strip()
#usar in para buscar
print('Seu nome tem Silva? {}'.format('silva' in nome.lower()))

