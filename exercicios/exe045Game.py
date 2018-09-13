from time import sleep
import random
# Regras do Jogo.
''' *Pedra empata com Pedra e ganha de Tesoura
    *Tesoura empata com Tesoura e ganha de Papel
    *Papel empata com Papel e ganha de Pedra'''

print('{:=^40}'.format(' JOKENPÔ '))
itens = ('Pedra', 'Papel', 'Tesoura')
computador = random.randint(0, 2)
print('''Suas Opções:
[ 1 ] Papel
[ 2 ] Pedra
[ 3 ] Tesoura''')

jogador = int(input('Qual a sua jogada?'))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!!')
print('-=' * 11)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-= ' * 11)

if computador == 0:#Computador jogou PEDRA.
    if jogador == 0:
      print('EMPATE!')
    elif jogador == 1:
      print('JOGADOR VENCE!')
    elif jogador == 2:
       print('COMPUTADOR VENCE!')
    else:
       print('JOGADA INVÁLIDA!')

elif computador == 1:#Computador jogou PAPEL.
    if jogador == 0:
        print('COMPUTADOR VENCE!')
    elif jogador == 1:
        print('EMPATE!')
    elif jogador == 2:
        print('JOGADOR VENCE!')
    else:
        print('JOGADA INVÁLIDA!')

elif computador == 2:#Computador jogou TESOURA.
    if jogador == 0:
        print('JOGAODOR VENCE!')
    elif jogador == 1:
        print('COMPUTADOR VENCE!')
    elif jogador == 2:
        print('EMPATE!')
    else:
        print('JOGADA INVÁLIDA!')



