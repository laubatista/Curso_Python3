
'''TUPLA - é uma variável composta que pode armazena vários valores,'''

#As tuplas são imutáveis.

lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata frita')

#Fatiamento
print(lanche) #Mostra todos os elementos da tupla.
print(lanche[3]) #Mostra apenas o elemento da posição 3.
print(lanche[2:]) #Mostra todos os elementos da posição 2 em diante.
print(lanche[:2]) #Mostra os elementos da posição 0 até a posição 2.
print(len(lanche))# Mostra a quantidade de elementos da tupla.
print(sorted(lanche)) #Mostra os elementos organizados por ordem alfabética.

#Percorrendo tuplas.

for comida in lanche: #Lista todas os alementos da tupla.
    print(f'Eu vou comer {comida}')

for cont in range(0, len(lanche)): #Lista todos os elementos da tupla mostrando a posição de cada um. .
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')

for pos,comida in enumerate(lanche): #Lista os elementos da tupla mostrado a posição de cada um.
    print(f'Eu vou comer {comida} na posição {pos}')

#Operações com tuplas

a = (2 ,5, 4)
b = (5, 8, 1, 2)
c = a + b # Junta os elementos da tupa a com a tupla b formando nova tupla c.
print(c.count(5)) #Mostra quantas vezes o elemento 5 aparece  na tuplas.
print(c.index(4)) #Mostra em qual posição está o elemento 4.

'''del (lanche) # Apaga a tupla da memória'''

#Deslocamento
print(c)
print(c.index(5 , 2))#mostra qual a posição do 5 apartir da posição 2.

