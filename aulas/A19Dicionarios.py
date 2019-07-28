#Declaração de um dicionário
'''
pessoas = {'Nome': 'Laudeine', 'Sexo': 'F', 'Idade': 26}
print(pessoas)
print(pessoas.keys())#Imprime as chaves
print(pessoas.values())#Imprime os valores
print(pessoas.items())#Imprime todos itens do dicionário
del pessoas['Sexo'] #Apaga o elemento sexo do dicionário.
pessoas['Nome'] = 'Leandro' # altera um elemento do dicionário.
'''
#Usando laços.
'''
for k, v in pessoas.items():
    print(f'{k} = {v}')
'''
'''
for k in pessoas.keys():
    print(k)
'''
#Dicionário dentro de uma lista.
'''
brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'Rio Grande do Norte', 'sigla': 'RN'}
brasil.append(estado1)
brasil.append(estado2)

print(brasil)
print(brasil[0]['uf'])
print(brasil[1]['sigla'])
'''
estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa:'))
    estado['sigla'] = str(input('Sigla do Estado:'))
    brasil.append(estado.copy())# O método copy cria ua cópia do dicionário dentro da lsita.
for e in brasil:
    #for k, v in e.items():
        #print(f'O compo {k} tem o valor {v}.')
    for v in e.values():
        print( v, end=' ')
    print()
