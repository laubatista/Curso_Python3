# Mostrar os 10 primeiros termos de uma  progressão aritimética.

print('Gerador de PA')
print('-=' * 10)
termo = int(input('1º Termo:'))
razao = int(input('Razão:'))

p = termo
cont = 1
while cont <= 10:
    print('{} ->'.format(p), end=' ')
    p += razao
    cont += 1

print('FIM')
