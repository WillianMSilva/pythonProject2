import math

numero = int(input('Digite um número inteiro: '))

print(" Para realizar a conversão\n 1 Binário\n 2 Hexadecimal\n 3 octagonal")

escolha = int(input('Qual opção de conversão: '))
#While estrutura de repetição caso o usuario selecione numero diferente.
while escolha > 3:
    escolha = int(input('Selecione de 1 a 3\n Qual opção de conversão: '))

if escolha == 1:
    #bin para transformar o numero binário e [2:] para cortar o inicio da informação
      print('numero {} em binario {}'.format(numero,bin(numero)[2:]))
elif escolha == 2:
    # hex para transformar o numero em hexadecimal e [2:] para cortar o inicio da informação

    print('numero {} em hexadecimal {}'.format(numero, hex(numero)[2:]))
elif escolha == 3:
    # oct para transformar o numero em octagonal e [2:] para cortar o inicio da informação
    print('numero {} em octagonal {}'.format(numero, oct(numero)[2:]))

