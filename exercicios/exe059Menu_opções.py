# Ler dois valores e mostre um menu. o programa deverá reslizar as operações que estão no menu.

num1 = int(input('Digite 1º valor:'))
num2 = int(input('Digite 2º valor:'))

opcao = 0
while opcao != 5:
    print('''Menu:
    [1]Somar
    [2]Multiplicar
    [3]Maior
    [4]Novo números
    [5]Sair do programa''')
    opcao = int(input('>>>>>>>> Qual a sua opção?'))
    if opcao == 1:
        soma = num1 + num2
        print('A soma dos valores {} e {} é {}'.format(num1, num2, soma))
    elif opcao == 2:
        mult = num1 * num2
        print('A multiplicação dos valores {} e {} é {}'.format(num1, num2, mult))
    elif opcao == 3:
        if num1 > num2:
            maior = num1
            print('Maior valor é o valor {}'.format(maior))
        else:
            maior = num2
            print('Maior valor é {}'.format(maior))
    elif opcao == 4:
        print('Informe os valores novamente:')
        num1 = int(input('Digite 1º valor:'))
        num2 = int(input('Digite 2º valor:'))

    elif opcao == 5:
        print('Finalizando...')
    else:
        print('Opção inválida! Tente novamente.')
    print('=-=' * 10)

print('Fim do programa!')

