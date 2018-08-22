from random import randint, choice
from datetime import date
valor = '153'
parte = "5"
valor +=parte

print(valor.isnumeric())

num = '7'
res = int(num) /2
print(type(res))

texto =  'Tres pratos de trigo para tigres tristes'
total = texto.upper().count(texto[0])
print(total)

frase = 'Curso em video de python'
separado = frase.split()
palavra = separado[2]
letra = palavra[3]
print(letra.upper())


num = randint(1 ,6)
res = num // 2
print(res)

ano = date.today().year
print(ano)

n = [2, 5, 9, 1, 4]
res = choice(n) % n[0]
print(res)