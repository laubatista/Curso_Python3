# Dizer se a frase é um palíndromo
frase = str(input('Digite uma frase:')).strip().upper()# Eliminou os espaços e colou em maiusculas
palavras = frase.split()#Separou as palavras
junto = ''.join(palavras)#juntou as palavras em um string
inverso = ''
inverso = junto[::-1]

'''
for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
'''
print('Você digitou a frase {} inverso {}'.format(frase, inverso))
if inverso == junto:
    print('\033[36mTemos um palídrommo!')
else:
    print('\033[031mA frase digitada não é um palídromo! ')




