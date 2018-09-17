
print('=+=' * 15)
print('TABUADA')
print('=+=' * 15)
print('Escolha a operação: 1 = Soma  2 = Subtração  3 = Multiplicação  4 = Divisão')
operacao = int(input('Operação:'))

n = int(input('Digite um número para ver sua tabuada:'))
for p in range(1, 11):
        if operacao == 1:
         resultado = n + p
         print('{} + {} = {}'.format(n, p, resultado))
        if operacao == 2:
            resultado = n - p
            print('{} - {} = {}'.format(n, p, resultado))
        if operacao == 3:
            resultado = n * p
            print('{} * {} = {}'.format(n, p, resultado))

        if operacao == 4:
            resultado = n / p
            print('{} / {} = {:.2f}'.format(n, p, resultado))





