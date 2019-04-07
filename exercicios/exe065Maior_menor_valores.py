# Lê vários valores e dizer a quantidade dos valores a média  entre eles e qual o maior.
resp = 'S'
soma = quant = 0
maior = 0
menor = 0
while resp in 'Ss':
    num = int(input('Digite um número:'))
    soma += num
    quant += 1
    if quant == 1:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num

    resp = str(input('Quer Continuar? [S/N]')).upper().strip()[0]

media = soma / quant

print('Você digitou {} números e a média foi {:.2f}'.format(quant, media))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))