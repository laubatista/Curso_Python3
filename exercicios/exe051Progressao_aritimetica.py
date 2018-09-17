#Prograssão aritimética de um número.

#Minha resolução.

n1 = int(input('1º Termo:'))
n2 = int(input('Razão:'))

for c in range(0, 10,):
    c = n1 + n2
    n1 = c
    c = n1 + n2
    print('{} + {} = {}'.format(n1, n2, c))

# Resolução do professor.
'''
décimo = n1 + (10 - 1) * n2
for c in range(n1, décimo + n2, n2 ):
    print('{}'.format(c), end=' -> ')
print(':)')
'''
