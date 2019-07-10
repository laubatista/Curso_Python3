'''Programa que vaii ler váios números e colocar em uma lista. Depois disso
crie duas listas extras que vão conter apenas os valores pares e os valores
impares digitdos, respectivamente. Ao final, mostre o conteúdo das três listas.'''

valores = []
pares = []
impares = []

while True:
    valores.append(int(input('Digite um valor:')))

    opcao = input('Quer continuar? [S/N]').strip().upper()
    if opcao in 'Nn':
        break

for num in valores:
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

print('=-' * 30)
print(f'A lista completa é {valores}')
print(f'A lista de pares é {pares}')
print(f'A lista de impares é {impares}')