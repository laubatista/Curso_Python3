from random import shuffle
g1 = input('1º grupo')
g2 = input('2º grupo')
g3 = input('3º grupo')
g4 = input('4º grupo')
g5 = input('5º grupo')

lista = [g1, g2, g3, g4, g5]

shuffle(lista)

print('A seguência de apresentação do grupos será:')
print(lista)