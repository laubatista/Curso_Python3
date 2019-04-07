
#Interrompendo o while

n = s = 0
while True:
    n = int(input('Digite um número:')) #vai ficar repetindo até o número digitado ser 999.
    if n == 999:
        break # quando digitar 999 ele para.
    s += n
#print('A soma vale {}'.format(s))
print(f'A soma vale {s}') # fstring nova pepi do python.

'''
#Exemplo de fstrig.

nome = 'Jose'
idade = 33
print(f'O {nome} tem {idade} anos. ')
'''










































