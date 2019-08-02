'''Faça um programa que tenha uma lista chamada números e duas funções chamadas
sorteia() e somapar(). A primeira função vair sortear 5 números e colocá-los dentro
de uma lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados
pela função anterior'''

from random import randint
from time import sleep
lista= list()


def sorteia():
    print(f'Sorteando 5 valores da lista', end=' ')
    for n in range(1, 6):
        num = randint(0, 20)
        lista.append(num)
        print(f'{num} ', end='', flush=True)
        sleep(0.3)
    print('PRONTO!')


def somapar(lst):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valores pares de {lista}, temos {soma}')


#Programa principal
sorteia()

somapar(lista)

