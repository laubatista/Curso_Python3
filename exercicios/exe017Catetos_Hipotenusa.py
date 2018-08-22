import math

'''cateto_oposto = float(input('Qual o comprimento do cateto oposto?'))
cateto_adj = float(input('Qual o comprimento do cateto adjacente?'))
hip = (cateto_oposto ** 2 + cateto_adj ** 2) ** (1/2)

print('A hipotenusa vai medir {:.2f}'.format(hip))'''

cateto_ops = float(input('Comprimento do cateto oposto?'))
cateto_adj = float(input('Comprimento do cateto adjacente? '))
hip = math.hypot(cateto_ops, cateto_adj)

print('A hipotenusa vai medir {:.2f}'.format(hip))