# Programa para contar quantas pessoas sao maiore e quantas são menores e idade.

from datetime import date

cont_maiores = 0
cont_menores = 0
ano_atual = date.today().year
for c in range(1, 7):
    ano = int(input('Em que ano a {}º pessoa nasceu?'.format(c)))
    if ano_atual - ano >= 18:
        cont_maiores += 1
    else:
        cont_menores +=1

print('\033[32mAo todo tivemos {} pessoas maiores de idade'.format(cont_maiores))
print('\033[34mE também tivemos {} pessoas menores de idade'.format(cont_menores))
