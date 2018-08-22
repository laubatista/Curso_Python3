preco = float(input('Qual o preço do produto? R$'))
des = float(input('Quanto porcento de desconto deseja aplicar'))

valordes = (preco* des)/100
novopreco = preco - valordes

print('Preço do produto = {} R$\nDesconto = {} %\nTotal a pagar =  {} R$,'.format(preco, des, novopreco))