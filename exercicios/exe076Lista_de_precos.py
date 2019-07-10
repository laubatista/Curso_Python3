
listagem = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00,
            'Mochila', 120.00,'Canetas', 22.30, 'Livro', 34.90, 'Marca texto', 3.00)

print('*' * 55)
print(f'{"LISTAGEM DE PRODUTOS E PREÇOS":^60}')
print('*' * 55)

for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}',end='')
    else:
        print(f'R${listagem[pos]:>7.2f}')

print('*' * 55)
