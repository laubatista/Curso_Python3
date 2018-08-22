
nome = str(input('Digite seu nome completo:')).strip()
print('Analisando seu nome:')

print('Nome em maiúsculas {}:'.format(nome.upper()))# Nome com todas as letras maiusculas
print('Nome em menúsculas {}:'.format(nome.lower())) #Nome com todas as letras minusculas
print('Nome tem {} letras:'.format(len(nome)-nome.count(' ')))#Quantas letras no total menos os espaços.
dividido = nome.split()
print('Seu primeiro nome é {} e ele têm {} letras'.format(dividido[0],len(dividido[0]))) #Qual o primeiro nome e quantas letras têm.
