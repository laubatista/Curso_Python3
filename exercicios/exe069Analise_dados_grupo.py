'''programa que ler a idade e sexo de várias pessoas, no final mostrar:
    A - Quantas pessoas tem mais de 18 anos
    B - Quantos homens foram cadastrados
    C - Quantas mulheres tem menos de 20 anos'''

print('-' * 30)
print(' '*5,'CADASTRE UMA PESSOA',' '*5)

maior_idade = 0
mulheres = 0
homens = 0
while True:
    print('-' * 30)
    idade = int(input('Idade:'))

    sexo = ' '
    while sexo not in 'MF': # só vai aceitar  a resposta quando for F/M
     sexo = (input('Sexo:[M/F]')).strip().upper()

    if idade >= 18:
        maior_idade += 1

    if sexo == 'M':
        homens += 1

    if sexo == 'F' and idade < 20:
         mulheres += 1

    opcao = ' '
    while opcao not in 'SN':
        opcao = (input('Quer continuar? [S/N]')).upper()
    if opcao == 'N':
        break
        print('ACABOU')

print('='* 7,'FIM DO PROGRAMA','='* 7,)
print('Total de pessoas maior de idade {}'.format(maior_idade))
print('Ao todo temos {} homens cadastrados'.format(homens))
print('E temos {} mulheres com menos de 20 anos'.format(mulheres))



