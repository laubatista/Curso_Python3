#
nomevelho = ''
maioridadehomens = 0
soma_idade = 0
média_idade = 0
totalmulher20 = 0
for p in range(1, 5):
    print('========={}º PESSOA ========='.format(p))
    nome = str(input('Nome:')).strip()
    idade = int(input('Idade:'))
    sexo = str(input('Sexo:')).strip()
    soma_idade += idade

    if p == 1 and sexo in 'Mm':
       maioridadehomens = idade
       nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomens:
       maioridadehomens = idade
       nomevelho = nome
    if sexo in 'Ff' and idade < 20:
       totalmulher20 += 1

média_idade = soma_idade / 4
print('A média de idade do grupo é de {} anos'.format(média_idade))
print('O homen mais velho do grupo têm {} anos e se chama {} !'.format(maioridadehomens, nomevelho))
print('Ao todo são {} mulheres como menos de 20 anos'.format(totalmulher20))




