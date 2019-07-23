'''Crie um programa que crie uma matriz de dimensão 3X3 e preencha
com valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta.'''
'''
matriz = list()

#cria listas dentro da lista matriz
for v in range(0,3):
    matriz.append([])

for cont in range(0, 3):
     matriz[0].append(int(input(f'Digite um valor para [0,{cont}]:')))
for cont in range(0, 3):
     matriz[1].append(int(input(f'Digite um valor para [1,{cont}]:')))
for cont in range(0, 3):
     matriz[2].append(int(input(f'Digite um valor para [2,{cont}]:')))

print(matriz[0])
print(matriz[1])
print(matriz[2])

'''

#Resolução do professor.

matriz2 = [[0, 0, 0,], [0, 0, 0], [0, 0, 0]]

for l in range(0 ,3): #percorre o que será as linhas.
    for c in range(0, 3):#percorre o que será as colunas.
        matriz2[l][c] = int(input(f'Digite um valor para [{l}, {c}]:'))
print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz2[l][c]:^5}]', end=' ')
    print()

