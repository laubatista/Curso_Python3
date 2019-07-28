'''Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre -os
em (com idade) em um dicionário se por acaso a CTPS for diferente de zero, o dicionário
recebrá também o ano de contratação e o saláio. Calcule e acrescente, além da idade,
com quantos anos a pessoa  vai se  aposentar.'''
from datetime import datetime
listagem = dict()

listagem['nome'] = str(input('Nome:'))
ano_nas = int(input('Ano de Nascimento:'))
listagem['idade'] = datetime.now().year - ano_nas
listagem['ctps'] =  ctps = int(input('Carteira de trabalho (0 não tem):'))

if listagem['ctps'] != 0:
    listagem['contratacao'] = contratacao = int(input('Ano de Contratação'))
    #idade_apos = (contratacao - ano_nas) + 35
    listagem['salario'] = salario =  float(input('Salaŕio:'))
    listagem['aposentadoria'] = (contratacao - ano_nas) + 35

print('-='*30)
for k, v in listagem.items():
    print(f'{k} têm valor {v}')
