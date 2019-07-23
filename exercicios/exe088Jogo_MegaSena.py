'''Faça um programa que ajude um jogador da mega sena a criar palpites.
O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para
cada jogo, cadastrando tudo em uma lista composta. '''
from random import randint

print('-'*30)
print('{:''^30}'.format('JOGA NA MEGA SENHA'))
print('-'*30)
jogos = list()

qtd = int(input('Quantos jogos você quer que eu sorteie?'))
print('{:-^40}'.format(f' SORTEANDO {qtd} JOGOS '))

for n in range(0, qtd):
    jogos.append([])

while qtd != 0:
    qtd -= 1
    for n in range(0, 6):
        num = randint(1, 60)

        if num not in jogos:
            num = randint(1, 60)
            jogos[qtd].append(num)

        else:
            num = randint(1, 60)
            jogos[qtd].append(num)

for c, v in enumerate(jogos):
    print(f'Jogo {c+1}: {v}')

print('{:-^30}'.format('< BOA SORTE! > '))