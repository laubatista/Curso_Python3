'''Faça um programa que leia o nome  e média de um aluno, guardando também a
situação em um dicionário. No final mostre o conteúdo da estrutura na tela'''

registro = dict()

registro['nome'] = str(input('Nome'))
registro['media'] = float(input(f'Média de {registro["nome"]}:'))
if registro['media'] >= 7:
    registro['situacao'] = 'Aprovado'
elif 5 <= registro['media']:
    registro['situacao'] = 'Recupearação'
else:
    registro['situacao'] = 'Reprovado'
print('-='*30)
for k , v in registro.items():
    print(f' --{k} é igual a {v}')