#Jogador vai tentar advinhar o número que o computador pensou e mostrar a quantidade de tentativas no final.

from random import randint

print('Sou o seu computador...')
print('Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue advinhar qual foi?')

palpite = int(input('Qual o seu palpite?'))

tentativas = 0
n = randint(0, 10)
while palpite < n:
    print('Mais... Tente mais uma vez.')
    palpite = int(input('Qual o seu palpite?'))
    tentativas += 1
while palpite > n:
    print('Menos... Tente mais uma vez.')
    palpite = int(input('Qual o seu palpite?'))
    tentativas +=1
print('Acertou com {} tentativas. Parabéns!'.format(tentativas))

# Resolução do professor.
'''computador  = randint(0, 10)
acertou  = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é o seu palpite?'))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez.')
        elif jogador > computador:
            print('Menos... Tente mais uma vez.')

print('Acertou com {} tentativas. Parabéns!'.format(palpites))'''



