salario = float(input('Salário atual do fucionário?'))

novosalario = (salario * 15/100) + salario

print('Com o reajuste de 15% ele passará a receber {:.2f} R$'.format(novosalario))