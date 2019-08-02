#Declaração de uma função com parâmetros.
'''
def soma(a, b):
    s = a +b
    print(s)

#programa Principal
soma(4, 5)
soma(10, 56)
soma(2, 6)
'''
#Empacotamento de parâmetro
'''
def contador (*num):#o num vai receber todos os valores passados com parâmetro e mostrar como uma tupla.~
    for valor in num:
        print(f'{valor} ', end='')
    print()

contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)
'''
#Funções com lista.
def dobra(lista):#função vai dobrar os valores que estiverem dentro da lista passada como parâmetro.
    pos = 0
    while pos < len(lista):
        lista[pos] *= 2
        pos +=1

valores = [2, 4, 6, 3, 5]
dobra(valores)
print(valores)
