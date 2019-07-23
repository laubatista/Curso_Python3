'''Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista.
No final mostre:
A - Quantas pessoas foram cadastradas.
B - Uma listagem com as pessoas mais pesadas.
C - Uma listagem com as pessoas mais leves. '''

listagem = list()
dados = list()
mais_pesado = list()
menos_pesado = list()
maior = menor = 0

#Cadastra e mostra a quantidade de pessoas escritas.
while True:
    dados.append(str(input('Nome:')))
    dados.append(float(input('Peso:')))
    listagem.append(dados[:])
    dados.clear()
    opcao = str(input('Quer continuar? [S/N]')).strip().upper()

    if opcao in 'Nn':
        break

print('=-'* 30)
print(f'Você cadastrou {len(listagem)} pessoas.')

#Confere qual o maior e menor peso e mostra o nome das pessoas com esses pesos.

for v in listagem:

    if v[1] >= maior:
        maior = v[1]
        menor = v[1]
        mais_pesado.append(v[0])

    if v[1] < menor:
        menor = v[1]
        menos_pesado.append(v[0])

print(f'O maior peso foi de {maior}Kg. Peso de{mais_pesado}.')
print(f'O menor peso foi de {menor}Kg. Peso de {menos_pesado}.')


