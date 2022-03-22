import math
print('Sabia o valor do seno, cosseno e tangente')
angulo = float(input('Digite o ângulo '))
#para achar o cosseno, seno e tangente no python transformar ângulo em radianos
radiano = math.radians(angulo)

print('Com o ângulo de {} o seno é {:.2f} '.format(angulo,math.sin(radiano)))
print('Com o ângulo de {} o cosseno é {:.2f} '.format(angulo,math.cos(radiano)))
print('Com o ângulo de {} o tangente é {:.2f} '.format(angulo,math.tan(radiano)))

