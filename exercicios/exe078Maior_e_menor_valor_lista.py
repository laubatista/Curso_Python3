'''Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final mostre qual o maior
e o menor valor digitado e as suas posições na lista. '''


valores = []
menor = maior = 0

for cont in range(0 ,5):
    valores.append(int(input(f'Digite um valor para a posição {cont}:')))

    if cont ==0:
        maior = menor = valores[cont]
    else:
        if valores[cont] > maior:
            maior = valores[cont]

        if valores[cont] < menor:
            menor = valores[cont]

print('=-' * 30)
print(f'Você digitou os valores {valores}')


print(f'O maior valor digitado foi {maior} nas posições', end=' ')
for p, v in enumerate(valores):
    if v == maior:
     print(p, end='..')


print(f'\nO menor valor digitado foi {menor} nas posições',end=' ')
for p, v in enumerate(valores):
    if v == menor:
     print(p, end='..')









