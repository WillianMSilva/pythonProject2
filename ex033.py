v1 = float(input('Digite um valor '))
v2 = float(input('Digite um valor '))
v3 = float(input('Digite um valor '))

if v1<v2 and v1<v3:
    menor = v1
if v2<v1 and v2<v3:
    menor = v2
if v3<v1 and v3<v2:
    menor = v3

if v1>v2 and v1>v3:
    maior = v1
if v2>v1 and v2>v3:
    maior = v2
if v3>v1 and v3>v2:
    maior = v3
print('O menor número é {}'.format(menor))
print('O maior número é {}'.format(maior))