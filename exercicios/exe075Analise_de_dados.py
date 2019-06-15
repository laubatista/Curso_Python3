
'''Programa que leia quatro valores pelo teclado e quarde-os em uma tupla. No final mostre:
   A - Quantas vezes apareceu o número 9
   B - Em que posição foi digitado o primeiro 3
   c - Quais foram os números pares'''

numeros = (int(input('Digite um número:')),
           int(input('Digite outro número')),
           int(input('Digite mais um número:')),
           int(input('Digite o último número:')))

print(f'Você digitou os valores {numeros}')
print(f'O valor 9 apareceu {numeros.count(9)} vezes.')
if 3 in numeros:
    print(f'O valor 3 apareceu na {numeros.index(3)}ª posição.')
else:
    print(f'O valor 3 não apareceu em nenhuma posição.')
print(f'Os valores pares digitados foram', end=' ')
for n in numeros:
    if n % 2 == 0:
        print(n, end=' ')




