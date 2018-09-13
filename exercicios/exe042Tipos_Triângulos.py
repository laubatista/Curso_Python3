print('-=-' * 30)
print('Analisando Triângulos')
print('-=-' * 30)

s1 = float(input('Primeiro Segmento:'))
s2 = float(input('Segundo Segmento:'))
s3 = float(input('Terceiro Segmento:'))

if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
    print('Os segmentos acima podem formar um triângulo ', end='')
    if s1 == s2 == s3:
        print('Equilátero!')
    elif s1 != s2 and s2 != s3 and s1 != s3:
        print('Escaleno!')
    else:
        print('Isósceles')
else:
    print('Os segmentos acima NÃO PODEM FORMAR triângulo!')

