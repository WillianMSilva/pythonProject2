nota1 = float(input("Primeira nota do aluno "))
nota2 = float(input("Segunda nota do aluno "))

# :.1f significa que depois do ponto flutante coloque apenas 1 digito colocar dentro das chaves.

print('A média entre {:.1f} e {:.1f} é {:.1f}'.format(nota1, nota2, ((nota1+nota2)/2)))
