
'''Escreva um programa que faça o computador "pensar" em um número inteiro 
entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. 
O programa deverá escrever na tela se o usuário venceu ou perdeu.'''

import random
from time import sleep

print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. ')
print('-=-' * 20)
num = int(input('Adivinhhe! qual número eu pensei?'))

print('PROCESSANDO...')
sleep(3)
n = random.randint(0, 5)

if num == n:
    print('Parabéns você acertou')
else:
    print('Que pena você perdeu! pensei em {}'.format(n))
