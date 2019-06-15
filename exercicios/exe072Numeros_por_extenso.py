'''Criar uma tupla preenchida com os números de zero a vinte por extenso
    O programa deverá ler um número entre 0 e 20 pelo teclado e mostra-lo por extenso.'''


numeros = ('zero','one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight','nine', 'ten','eleven', 'twelve', 'thirteen'
           ,'fouteen', 'fifteen', 'sixteen', 'seventeen', 'nineteen', 'twenty')


while True:
    num = int(input('Digite um número entre 0 e 20:'))

    if  num < 0 or num > 20:
        print('Número inválido! Tente novamente.')

    else:
        print(f'Você digitou o número:{numeros[num]}')

    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Deseja continuar?[S/N]')).upper().strip()[0]

    if opcao == 'N':
        break

print('{:=^30}'.format('PROGRAMA FINALIZADO'))




