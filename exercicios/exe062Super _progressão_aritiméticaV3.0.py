#

print('Gerador de PA')
print('-=' * 10)
termo = int(input('1º Termo:'))
razao = int(input('Razão:'))

p = termo
cont = 1
total = 0
mais = 10
while mais !=0:
    total = total + mais
    while cont <= total:
        print('{} ->'.format(p), end=' ')
        p += razao
        cont += 1

    print('PAUSA')
    mais = int(input(('Quantos termos você quer mostrar a mais?')))
print('Progressão finalizada com {} termos mostrados.'.format(total))
print('FIM')