
from datetime import date
ano_nas = int(input('Digite o ano de nascimento:'))
ano_atual = date.today().year

idade = ano_atual - ano_nas

print('O atleta tem {} anos.'.format(idade))

if idade <= 9:
    print('Categoria Mirrim !')

elif idade <= 14:
    print('Categoria Infantil!')

elif idade <= 19:
    print('Categoria Junior!')

elif idade <= 20:
    print('Categoria Sênior!')

else:
    print('Categoria Master!')