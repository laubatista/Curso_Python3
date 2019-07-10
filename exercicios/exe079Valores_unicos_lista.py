'''programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
 Casoo u número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos
 digitados, em ordem crescente. '''

valores = []
while True:
    num = int(input('Digite um valor:'))
    if num in valores:
        print('Valor duplicado! Não vou adicionar..')

    else:
      valores.append(num)
      print('Valor adicionado com sucesso!')

    opcao = ' '
    while opcao not in 'S/N':
        opcao = input('Quer continuar? [S/N]').strip().upper()[0]
    if opcao == 'N':
        break

print('=-' * 30)
valores.sort()
print(f'Você digitou os valores {valores}')







