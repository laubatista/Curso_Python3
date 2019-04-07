''' Programa que mostre a tabudada de varios números um de cada vez e seja interrompido
quando o número for negativo.
'''

while True:
    print('==' * 20)
    n = int(input('Quer ver a tabuada de qual valor?'))
    print('==' * 20)
    if n < 0:
        print('PROGRAMA TABUADA ENCERRADO. volte sempre!')
        break

    for num in range (1, 11):
        resultado = n * num
        print(f'{n} x {num} = {resultado}')







