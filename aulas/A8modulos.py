#importando todas as funcionalidades da biblioteca.

'''
import math
num = int(input('Digite um número:'))
raiz = math.sqrt(num)
print('A raiz de {} é igual a {:.3f}'.format(num, raiz))
print('A raiz de {} é igual a {}'.format(num, math.ceil(raiz)))
print('A raiz de {} é igual a {}'.format(num, math.floor(raiz)))
'''
# Impotando só módulos .
'''
from math import sqrt,floor
num = int(input('Digite um numero:'))
raiz = sqrt(num)
print('A raiz de {} é igual a {:.2f}'.format(num,floor(raiz)))
'''
import random
num = random.randint(1, 50)
print(num)