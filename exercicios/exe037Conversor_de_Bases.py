#Conversão de números
from time import sleep

num = int(input('Digite o número que deseja converter:'))

print('Escolha a base para conversão:\n'
'1= Binário\n' 
'2= Octal\n'
'3= Hexadecimal ')

base = int(input('Base escolhida  '))

print('Convertendo...')
sleep(2)

if base == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(num, bin(num)[2:]))

elif base == 2:
     print('{} convertido para OCTAL é igul a {}'.format(num, oct(num)[2:]))

elif base == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(num, hex(num)[2:]))

else:
    print('Opção inválida')

