#import random serve para trazer o random.choice para sorteio.
import random
aluno1 = str(input("nome do aluno "))
aluno2 = str(input("nome do aluno "))
aluno3 = str(input("nome do aluno "))
aluno4 = str(input("nome do aluno "))

lista = [aluno1,aluno2,aluno3,aluno4]
print("o escolhido foi {} ".format(random.choice(lista)))
