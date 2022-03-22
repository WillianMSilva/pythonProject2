# sinais para processos matemáticos
# soma = +
# subtração = -
# multiplicação = *
# divisão = /
# Potência = **
# divisão inteira = //
# resto da divisão = %

# Ordem de precedência os operadores que são executados dentro de uma expressão matemática
# primeira = parenteses ()
# segunda = potênciação **
# terceiro = multiplicação (*) divisão (/) divisão inteira (//) resto da divisão (%)
# quarta = soma (+) subtração (-)

v1 = float(input('Digite um valor '))
v2 = float(input('Digite outro valor'))

adição = v1 + v2
subtração = v1 - v2
sub = v2 - v1
multiplicação = v1 * v2

print(' O valor da sua soma de {} + {} igual {}'.format(v1, v2, adição))
print(' O valor da sua subtração de {} - {} igual {}'.format(v1, v2, subtração))

# Usado IF para condição quando o valor 2 for maior que valor 1 trocar a ordem dos valores
# para não dar um número negativo.
# sempre que usar o IF inserir : no final.

if v2 > v1:
    print('O valor da sua subtração invertida de {} - {} igual {}'.format(v2, v1, sub))
print(' O valor da sua multiplicação de {} x {} igual {}'.format(v1, v2, multiplicação))
