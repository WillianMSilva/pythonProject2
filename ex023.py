numero = int(input('Digite um número: '))
#Realizado a divisão e inserir o módulo para "pegar" somente o número necessário.
u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10
print('Analisando o número {}'.format(numero))
print('unidade {}'.format(u))
print('dezena {}'.format(d))
print('centena {}'.format(c))
print('milhar {}'.format(m))
