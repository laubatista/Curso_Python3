#Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

num = int(input('Digite um número:'))

if num % 2 == 0:
    print('O numero {} é Par!'.format(num))

else:
    print(' O número  {} é Impar!'.format(num))
