peso = float(input('Qual o seu peso?'))
altura = float(input('Qual a sua altura?'))

imc = peso / (altura ** 2)

print('O IMC dessa pessoa é {:.2f}'.format(imc))

if imc < 18.5:
    print('Abaixo do peso ideal!')

elif imc > 18.5 and imc < 25:
    print('Peso Ideal!')

elif 25 <= imc < 30:
    print('Sobrepeso!')

elif 30 <= imc < 40:
    print('Obesidade!')

else:
    print('Obesidade Mórbida Cuidado!')
