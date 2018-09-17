#Estrutura Condicional
n1 = float(input('Digite a primeira nota:'))
n2 = float(input('Digite a segunda nota:'))
m = (n1 + n2)/2
#condição simples
if m >= 6.0:
    print('Aluno aprovado')

#Condição composta
if m >= 10:
    print('Parabéns!!!')

else:
    print('Mehore!')

#Condição simplificada
print('Aprovado' if m>= 6.0 else 'Reprovado')