#Desenvolva um programa que pergunte a distância de uma viagem em Km.
#Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km
#E R$0,45 parta viagens mais longas.

dist = float(input('Digite a distancia da viagem em Km:'))

if dist <= 200:
    print('Custo da passagem  = R${:.2f}'.format(dist * 0.50))
else:
    print('Custo da passagem = R${:.2f}'.format(dist * 0.45))
