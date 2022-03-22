print ("="*30)
print('Analisador de triângulos')
print ("="*30)
r1 = float(input('Insira um número '))
r2 = float(input('Insira um número '))
r3 = float(input('Insira um número '))


if r1 < r2+r3 and r2 < r1+r3 and r3 < r1+r2 and r1 == r2 == r3:
    print('Os segmentos acima podem formar um triângulo!Equilátero')
elif r1 < r2+r3 and r2 < r1+r3 and r3 < r1+r2 and r1 == r2 != r3 or r2 == r3 != r1 or r3 == r1 !=r2:
    print('Os segmentos acima podem formar um triângulo Isósceles!')
elif r1 < r2+r3 and r2 < r1+r3 and r3 < r1+r2 and r1 != r2 != r3 != r1:
    print('Os segmentos acima podem formar um triângulo Escaleno!')
else:
    print('Os segmentos acima não podem formar um triângulo!')
