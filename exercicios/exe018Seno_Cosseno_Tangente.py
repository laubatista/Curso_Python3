import math
angulo = float(input('Digite o ângulo que você deseja:'))
seno = math.sin(math.radians(angulo))
cos = math.cos(math.radians(angulo))
tang = math.tan(math.radians(angulo))

print('O ângulo de {} têm o SENO de {:.2f}'.format(angulo, seno))
print('O ângulo de {} têm COSSENO de {:.2f}'.format(angulo, cos))
print('O ângulo de {} têm TANGENTE e {:.2f}'.format(angulo,tang))