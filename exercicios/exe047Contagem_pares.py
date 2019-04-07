#Mostrar todos os números pares no intervalo de 1 a 50.
# 1º exemplo
# Nesta forma usa mais processador, pois faz mais interações.
'''
for n in range(1, 51):
    if n % 2 == 0:
      print(n, end=' ')
'''

# 2º exemplo
for n in range(2, 50, 2):
    print(n, end=' ')
print('ACABOU!')