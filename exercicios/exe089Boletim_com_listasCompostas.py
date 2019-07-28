'''Crie um programa que leia o nome e duas notas de vários alunos e guarde
tudo em um lista composta. No final, mostre um boletim contendo  média de cada um e permita
que o usuário possa mostrar as notas de cada aluno individualmente.'''

boletim = []
qtd = 0
media = 0
while True:
    nome = str(input('Nome:'))
    nota1 = float(input('Nota 1:'))
    nota2 = float(input('Nota 2:'))
    media = (nota1 + nota2) / 2
    boletim.append([nome, [nota1, nota2], media])

    opcao = str(input('Deseja continuar? [S/N]')).strip().upper()

    if opcao in 'Nn':
     break

print('-='* 30)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-'*30)
for i, a in enumerate(boletim):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-' * 35 )
    opc = int(input('Mostrar as notas de qual aluno? (999 interrompe):'))
    if opc == 999:
        print('FINALIZANDO...')
        break
    if opc <= len(boletim) -1:
        print(f'Notas de {boletim[opc][0]} são {boletim[opc][1]}')

print('<<< VOLTE SEMPRE >>>')









