'''Faça um programa que tenha uma função chamada contador(), que receba três
parâmetros: inicio, fim, e passo e realize a contagem.
Seu programa tem que realizar três contagens  através da função criada:
A - De 1 até 10. de 1 em 1.
B - De 10 até 0, de 2 em 2.
C - Uma contagem personalizada.'''
from time import sleep


def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print('-='*30)
    print(f'Contagem de {i} até {f} de {p} em {p}.')
    sleep(0.5)

    if i < f:
        cont = 1
        while cont <= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont += p
        print('FIM!')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont -= p
        print('FIM!')


#Programa principal.
contador(1, 10, 1)
contador(10, 0, -2)
print('-='*30)
print('Agora é sua vez de personalizar contagem!')
inicio = int(input('Inicio:'))
fim = int(input('Fim:'))
passo = int(input('Passo'))
contador(inicio, fim, passo)
