
#Contagem regressiva com intervalo de 1 segundo.
from time import sleep

print('Contagem regressiva para a queima de fogos!')
for cont in range(10, -1, -1):
    sleep(0.5)
    print(cont)
print('BUM! BUM! BUUMM!')