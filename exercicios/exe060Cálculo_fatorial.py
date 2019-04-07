#Ler um número e mostrar o seu fatorial.

from math import factorial

num = int(input('Digite um número para ver seu fatorial.'))

# 1º resolução:
'''f = factorial(num)
print('O fatorial de {} é {}'.format(num, factorial()))
'''
# 2º REsolução:

c = num
f =1
print('Calculando {}! = '.format(num), end='')
while c > 0:
   print('{}'.format(c), end=' ')
   print('x' if c > 1 else '=', end=' ')
   f *= c
   c -= 1
print('{}'.format(f))


# 3º Resolução:
'''
f = 1
for c in range(0, num):

   f *= num
   num -= 1

print('{}'.format(f))
print(len(str(f)))


'''
