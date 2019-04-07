
num = int(input('Digite um número [999 para parar]:'))
soma = num
cont = 0
# Minha resolução:

while num != 999:
    num = int(input('Digite um número [999 para parar]:'))
    cont += 1
    if num == 999:
        print('Parou.')
    else:
        soma += num
        num = soma
print('Você digitou {} números  e a soma entre eles foi {}'.format(cont, soma))

'''
# Resolução do professor.
soma = 0
while num != 999:
    soma +=num
    cont +=1
    num = int(input('Digite um número [999 para parar]:'))
print('Você digitou {} números  e a soma entre eles foi {}'.format(cont,soma))
'''