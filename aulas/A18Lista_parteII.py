#Listas dentro de listas.
'''
teste = list()
teste.append('Laudeine')
teste.append(26)
galera = list()
galera.append(teste[:])
print(galera)

teste[0] = 'Maria'
teste[1] = 22

galera.append(teste[:])
print(teste)
print(galera)
'''
#Criando varias listas dentro de uma lista.
'''
galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
for p in galera:
    #print(p)
    print(f'{p[0]} tem {p[1]} anos de idade.')
print(galera)
'''
#Exemplo 03

galera = list()
dados = list()
maior_idade = menor_idade = 0
for c in range(0, 4):
    dados.append(str(input('Nome:')))
    dados.append(int(input('Idade:')))
    galera.append(dados[:])#Cria uma cópia da lista dados dentro da lista galera
    dados.clear()#Apaga as informações da lista dado

for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade ')
        maior_idade += 1
    else:
        print(f'{p[0]} é menor de idade.')
        menor_idade +=1

print(f'Temos {maior_idade} maiores e {menor_idade} menores de idade.')

