
#Exemplo - 01
'''
for c in range(1, 7):conta de 1 a 6
#for c in range (7, 0, -1):conta ao contrário
#for c in range(0, 7, 2): conta de 0 a 7 pulando 2.
#   print(c)
#print('fim')
'''

#Exemplo - 02
''''
i = int(input('Inicio:'))
f = int(input('Fim:'))
p = int(input('Passo:'))

for c in range(i, f+1, p):
    print(c)
print('fim')
'''
# Exemplo - 03
s = 0
for c in range(0, 4):
    n = int(input('Digite um valor:'))
    s +=n
print('O somatóriode todos os valores foi {}'.format(s))