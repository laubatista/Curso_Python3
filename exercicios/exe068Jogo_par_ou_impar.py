''' Fazer um jogo de par ou impar com o computador. O jogo será interrompido quando o joogador perder
mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
'''
from random import  randint

print('=-=' * 20)
print(' '*15,'VAMOS JOGAR PAR OU ÍMPAR', ' '*8)
print('=-=' * 20)

vitorias = 0

while True:
    jogador = int(input('Diga um valor:'))
    computador = randint(0, 11)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'P/I':
        tipo = str(input('Par ou Impar? [P/I]')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total}', end=' ')
    print('DEU PAR ' if total % 2 == 0 else 'DEU IMPAR')
    if tipo == 'P':
        if total % 2 ==0:
         vitorias += 1
         print('Você VENCEU!')

        else:
            print('Você PERDEU!')
            print('=-=' * 20)
            break
    if tipo == 'I':
        if total % 2 == 1:
         vitorias += 1
         print('Você VENCEU!')

        else:
            print('Você PERDEU!')
            print('=-=' * 20)
            break

    print('Vamos jogar novamente..')
print(f'GAME OVER! Você venceu {vitorias} vezes.')



