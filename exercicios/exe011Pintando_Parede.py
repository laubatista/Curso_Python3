larg = float(input('Quantos metros de largura têm a parede? '))
alt = float(input('Quantos metros de altura têm a parede?'))

area = larg * alt
tinta = 2

qnt =  area / 2

print('A área total da parede é:{}m'.format(area))
print('Tinta necessária para pintar a parede é {} litros'.format(qnt))
