#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
nome = str(input('Digite seu nome:')).strip()
print('Analisando..')

pos = nome.split()
print('Seu primeiro nome é: {}'.format(pos[0]))
print('Seu ultimo nome é:{}'.format(pos[len(pos)-1]))

