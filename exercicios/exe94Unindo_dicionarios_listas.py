'''Crie um programa que leia nome, sexo, e idade  de várias pessoas, guardando os dados de cada pessoa em uma lista.
No final, mostre:
A - Quantas pessoas foram cadastradas.
B - média de idade do gurpo
C - Uma lista com todas as mulheres
D - Uma lista com todas as pessoas com idade acima da média'''

dados = dict()
listagem = list()
media = soma = 0
while True:
    dados['nome'] = str(input('Nome:'))
    while True:
        dados['sexo'] = str(input('Sexo: [M/F]')).upper()[0]
        if dados['sexo'] in 'MF':
            break
        print('ERRO! por favor, digite apenas M ou F. ')
    dados['idade'] = int(input('Idade'))
    soma += dados['idade']
    listagem.append(dados.copy())
    while True:
        opc = str(input('Quer continuar? [S/N]')).upper()[0]
        if opc in 'SN':
            break
        print('ERRO! Responda apenas S ou N. ')
    if opc == 'N':
        break
print('-='* 30)
print(f'A) Ao todos temos {len(listagem)} pessoas cadastrada.')
media = soma / len(listagem)
print(f'B) A média de idade é de {media:5.2f} anos')
print(f'C) As mulheres cadastradas foram:', end=' ')
for p in listagem:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]}', end=' ')
print()
print('f D) Listas das pessoas que estão acima da média:')
for p in listagem:
    if p['idade'] >= media:
        for k, v in p.items():
            print(f'{k} = {v}', end=' ')
        print()
print('<<< ENCERRADO >>>')



