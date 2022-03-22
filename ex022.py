#usar o .strip para tirar os espaços excendentes
nome = str(input('Digite seu nome completo: ')).strip()
print('analisando seu nome...')
#Códigos abaixo para deixar o nome em maiusculas (upper) ou minusculas (lower)
print('Seu nome em maiúsculas é {} '.format(nome.upper()))
print('Seu nome em minúsculas é {} '.format(nome.lower()))
#usar o len para contar as letras e subtrair com count para tirar os espaços entre os nomes
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(" ")))
#usar .find para procurar no primeiro espaço
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))