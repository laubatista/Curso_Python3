'''Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros
com valores inteiros.
Seu programa têm que analisar todos os valores e dizer qual deles é o maior.'''
from time import sleep

def maior(*num):
    cont = maior_valor = 0
    print('-='*30)
    print('Analisando os valores passados....')
    for valor in num:
        print(f'{valor} ', end='', flush=True)
        sleep(0.3)
        if cont == 0:
            maior_valor = valor
        else:
            if valor > maior_valor:
                maior_valor = valor
    print(f'Foram informados {cont} valores ao todo.')
    print(f' O maio valor foi de {maior_valor}')

#Programa principal
maior(2, 9, 4, 5, 7, 1 )
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()