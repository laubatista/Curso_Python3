'''Programa que simula um caixa eletrônico.
 A - Pergunte ao usuário qual será o valor a ser sacado.
 B - Informar quantas cédulas de cada valor serão entregues.
 C - Considerar que o caixa possui cádulas de R$50, R$20, R$10 e R$1.'''

print('-' * 30)
print(' '*7,'BANCO DA LAU',' '*5)
print('-' * 30)

#Resolução do professor.
valor = int(input('Que valor você que sacar? R$'))
total = valor
cedula = 50
tcedula = 0

while True:
    if total >= cedula:
        total -= cedula
        tcedula += 1

    else:
        if tcedula > 0:
            print(f'Total de {tcedula} cédulas de R$ {cedula}')

        if cedula == 50:
            cedula = 20

        elif cedula == 20:
            cedula = 10

        elif cedula == 10:
            cedula = 1

        tcedula = 0

        if total == 0:
            break

print('Volte sempre ao BANCO DA LAU! Tenha um bom dia!')





