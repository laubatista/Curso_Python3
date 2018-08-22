'''Escreva um programa que pergunte o salário de um funcionário e calcule
o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento
de 10%. Para os inferiores ou iguais, o aumento é de 15%.
'''
import math
salario = float(input('Qual o valor do seu salário?'))


if salario <= 1250.00:
    novosalario = salario + (salario * 15 /100)

else:
    novosalario = salario + (10/100 * salario)

print('O novo valor do seu salário é R${:.2f}'.format(novosalario))
