'''
#Declaração de uma lista.
num  = [2, 5, 9, 1]
num[2] = 3 #substitui o valor da posição por 3.
num.append(7)#adiciona o valor 7 na liista.
num.sort()#coloca os valores na ordem crescente.
num.sort(reverse=True)#coloca os valores na ordem decresente.

print(num)

num.insert(2, 0)#inseri o elemento 0 na posição 2 e depois alinha os índices.
print(num)
num.pop()#exclui o ultimo elemento da lista.
num.pop(2)#exclui o elemento do indice 2.
num.remove(2)#procura na lista e primeira ocorrência do valor e elemina da lista.

print(num)
print(f'Essa lista tem {len(num)} elementos.')

#usando estrura condicional em uma lista.
if 4 in num:
    num.remove(4)
else:
    print('Não achei o número 4')
'''
#Usando estrutura de controle em uma lista.
valores = []
'''
valores.append(5)
valores.append(9)
valores.append(3)

for v in valores:
    print(f'{v}...',end='')

#Mostrando os indices e os valores.
for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
'''
#pegando valores pelo teclado.
for cont in range(0, 5):
    valores.append(int(input('Digite um valor:')))
print(valores)

#criando uma cópia da lista

novalista = valores[:]#copia todos os elemento da lista valores para a novalista.
print(novalista)