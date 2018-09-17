#Calcular a soma e todos os números impares que são multiplos de três no itervalo de 1 a 500.
# Minha resolução.
'''
s = 0
for n in range(1, 501):
   if n % 2 != 0:
       impar = n

       if impar % 3 == 0:
          print(impar)
          s +=impar
print('A soma de todos os impares multiplos de três é: {}'.format(s))
'''

# Resolução do professor
soma = 0
cont = 0 # conta os valores impares
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont = cont + 1
        soma = soma + c
print('A soma de todos os {} valores solicitados é {}'.format(cont, soma))
