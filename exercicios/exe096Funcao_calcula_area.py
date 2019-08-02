'''Faça um programa que tenha uma função chamada área , que receba as dimenções de
um terreno retangular (largura e comprimento) e mostre a área do terreno. '''

def area (a, b):
    tam = a * b
    print(f'A área de um terreno {a}x{b} é de {tam:5.2f} metros quadrados. ')

#Programa principal.
print('Controle de Terrenos')
print('='*30)
larg = float(input('LARGURA (m):'))
comp = float(input('COMPRIMENTO (m):'))
area(larg, comp)
