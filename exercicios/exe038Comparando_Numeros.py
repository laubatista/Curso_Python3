#Comparando números.

num1 = int(input('Digite o primeiro numero:'))
num2 = int(input('Digite o segundo número'))

if num1 > num2:
    print('O primeiro valor é maior.')
elif num1 < num2:
    print('O segundo valor é maior.')

elif num1 == num2:
    print('Não existe valor maior, os dois valores são iguais.')
