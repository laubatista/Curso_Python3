'''Aprimore o desafio anterior, mostrando no final:
A - A soma dos valores pares digitados.
B - A soma dos valores da terceira coluna.
C - O maior valor da segunda linha.'''
#Minha resolução.
'''
matriz = list()
maior = 0
soma = 0
somapar = 0

#cria listas dentro da lista matriz
for v in range(0,3):
    matriz.append([])

for cont in range(0, 3):
     matriz[0].append(int(input(f'Digite um valor para [0,{cont}]:')))

for cont in range(0, 3):
     matriz[1].append(int(input(f'Digite um valor para [1,{cont}]:')))

for cont in range(0, 3):
     matriz[2].append(int(input(f'Digite um valor para [2,{cont}]:')))

#Verifica qual o maior valor da segunda linha da coluna.
for p in matriz[1]:
    if p > maior:
        maior = p

#Faz a soma dos elementos da terceira coluna.
for p in matriz:
    soma += p[2]

#Verifica e faz a soma dos valores que são pares.
for p in matriz:
    if p[0] % 2 == 0:
        somapar += p[0]
    if p[1] % 2 == 0:
        somapar +=p[1]

    if p[2] % 2 ==0:
        somapar += p[2]

print('=-' * 30)
print(f'{matriz[0]}\n{matriz[1]}\n{matriz[2]}')
print('=-' * 30)
print(f'A soma dos valores pares é de {somapar}')
print(f'A soma dos valores da terceira coluna é {soma}')
print(f'O maior valor da segunda linha é {maior}')
'''
#Resolução do professor.
matriz2 = [[0, 0, 0,], [0, 0, 0], [0, 0, 0]]
soma_pares = maior = soma_coluna = 0

for l in range(0 ,3): #percorre o que será as linhas.
    for c in range(0, 3):#percorre o que será as colunas.
        matriz2[l][c] = int(input(f'Digite um valor para [{l}, {c}]:'))
print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz2[l][c]:^5}]', end=' ')
        if matriz2[l][c] % 2 == 0:
            soma_pares += matriz2[l][c]
    print()
print('-='* 30)
print(f'A soma dos valores pares é {soma_pares}')
for l in range(0, 3):
    soma_coluna += matriz2[l][2]
print(f'A soma dos valores da terceira coluna é {soma_coluna}')
for c in range(0, 3):
    if c == 0:
        maior = matriz2[1][c]
    elif matriz2[1][c] > maior:
        maior = matriz2[1][c]
print(f'O maior valor da segunda linha é {maior}')