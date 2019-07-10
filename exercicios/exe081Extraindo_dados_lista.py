'''Programa que vai ler vários números e colocar em uma lista. Depois mostre:
A - Quantos números foram digitados
B - A lista de valores, ordenada de forma decrescente
C - Se o valor 5 foi digitado e está ou não na lista'''

numeros = []
while True:
    numeros.append(int(input('Digite um valor:')))

    opcao = input('Quer continuar? [S/N]').strip().upper()
    if opcao in 'Nn':
        break

numeros.sort(reverse=True)
print('=-' * 30 )
print(f'Você digitou {len(numeros)} elementos.')
print(f'O valores em ordem decrescente são: {numeros}')

if 5 in numeros:
    print(f'O valor 5 faz parte da lista! Aparece {numeros.count(5)} vezes.')

else:
    print(f'O valor 5 não foi encontrado na lista.')

