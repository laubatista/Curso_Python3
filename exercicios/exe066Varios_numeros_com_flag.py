''' *Criar um programa que leia vários números.
    *Parar quando 999 for digitado.
    *Mostrar quantos números foram digitados.
'''
soma = 0
qnt = 0
while True:
    numero = int(input('Digite um valor (999 para parar):'))

    if numero == 999:
        break
    qnt += 1
    soma += numero
print('A soma dos {} valores foi {}!'.format(qnt,soma))


