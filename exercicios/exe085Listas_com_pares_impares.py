'''Crie um programa onde o usuárui possa digitar sete valores numéricos e cadastre-os em uma lista única
 que mantenha separados os valores pares e ímpares. No final mostre os valores
 pares e ímpares em ordem crescente'''


list_numeros = [[], []] #Lista que vai receber as listas pares e impares.

for n in range(1, 8):
    num = int(input(f'Digite o {n}ª valor:'))

    if num % 2 == 0:
       list_numeros[0].append(num)
       list_numeros[0].sort()

    if num % 2 != 0:
        list_numeros[1].append(num)
        list_numeros[1].sort()

print('=-' * 30)
print(f'Os valores pares digitados foram:{list_numeros[0]}')
print(f'Os valores impares digitados foram{list_numeros[1]}')


