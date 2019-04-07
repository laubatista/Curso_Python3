#Verificar quantas vezes aparece a letra 'a' e em que posição aparece

frase = str(input('Digite uma frase:').strip().upper())

print('A letra a aparece {} vezes na frase'.format(frase.count('A')))
print('O primeiro A apareceu na posição {}:'.format(frase.find('A')+1))
print('O ultimo A aparece na posição {}'.format(frase.rfind('A')+1))