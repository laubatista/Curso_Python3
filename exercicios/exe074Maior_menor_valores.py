'''Criar um programa que gere cinco números aleatórios e coloque-os em uma tupla.
   A - Mostrar a listagem dos números gerados
   B - Mostrar o maior e o menor valor'''

from random import randint

numeros = (randint(1,11), randint(1,11), randint(1,11), randint(1,11), randint(1,11))

print(f'Os valores sorteados foram: ',end=' ')
for num in numeros:
    print(f'{num} ', end='')

#Funções do python para ver o maior e o menor valor.
print(f'\nO maior valor sorteado foi {max(numeros)}')
print(f'O menor valor sorteado foi {min(numeros)}')

maior = 0
menor = 0

for pos, valor in enumerate (numeros):

    if (numeros[pos]) > maior:
        maior = (numeros[pos])
        menor = maior

    if (numeros[pos]) < menor:
        menor = (numeros[pos])

print(f'O maior valor sorteado foi {maior}:')
print(f'O menor valor sorteado foi {menor}:')