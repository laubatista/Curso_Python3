'''Desenvolva um programa que leia o comprimento de três retas e diga
 ao usuário se elas podem ou não formar um triângulo.
'''
print('-=-' * 30)
print('Analisando Triângulos')
print('-=-' * 30)

s1 = float(input('Primeiro Segmento:'))
s2 = float(input('Segundo Segmento:'))
s3 = float(input('Terceiro Segmento:'))

if s1 < s2 and s2 < s1 + s3 and s3 < s1 + s2:
    print('Os segmentos acima PODEM FORMAR triângulo!')

else:
    print('Os segmentos acima NÃO PODEM FORMAR triângulo!')





