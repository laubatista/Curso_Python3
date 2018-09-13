
from datetime import date
ano_nas = int(input('Digite o ano de nascimento:'))
ano_atual = date.today().year

idade = ano_atual - ano_nas

if idade < 18:
    saldo = 18 -idade
    print('Faltam {} anos! para o alistamento'.format(saldo))

    ano = ano_atual + saldo
    print('Seu alistamento será em {}.'.format(ano))

elif idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')

elif idade > 18:
    saldo = idade - 18
    print('Você já deveria ter se alistado há {} anos!'.format(saldo))
    ano = ano_atual - saldo
    print('Ano do alistamento {}.'.format(ano))
