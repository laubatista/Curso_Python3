real = float(input('Quantos reais você tem na carteira?'))
dolar =  real / 3.76


print('Com a quantia de R${}, você pode comprar U$${:.3f} dolares'.format(real, dolar))