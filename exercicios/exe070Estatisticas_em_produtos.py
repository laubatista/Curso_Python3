'''Um programa que leia o nome e preço de vários produtos e ao final:
   A - Qual o tatal gasto na compra
   B - Quanto produtos custam mais de 1000 reais
   C - Qual é o nome do produto mais barato'''


print('{:-^40}'.format('LOJÃO DA LAU '))

total = maior_mil  = barato = cont = 0
maisbarato = ' '
while True:
    produto_nome = input('Nome do Produto:').upper()
    preco = float(input('Preço: R$'))
    cont += 1
    total += preco

    if preco > 1000:
        maior_mil +=1

    if cont == 1 or preco < barato:
        barato = preco
        maisbarato = produto_nome
    opcao = ' '
    while opcao not in 'S/N':
     opcao = input('Quer continuar? [S/N]').strip().upper()[0]
    if opcao == 'N':
        break

print('-' * 5, 'FIM DA COMPRA', '-' * 5)
print('Total da compra foi R${}'.format(total))
print('Temos {} produtos custanto mais de R$1000.00'.format(maior_mil))
print('O produto mais barato foi {} que custa R${}'.format(maisbarato,barato))


