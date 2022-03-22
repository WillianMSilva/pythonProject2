nome = str(input('Digite seu nome completo: ')).strip()
#.split separa o nome em partes
n = nome.split()
#para aparecer o primeiro nome na ordem é zero.
print("Muito prazer em te conhecer \n"'Seu primeiro nome é {}'.format(n[0]))
#último nome para aparecer idependente do tamanho usa o len de n-1 para buscar o último nome.
print('Seu último nome é {}'.format(n[len(n)-1]))


