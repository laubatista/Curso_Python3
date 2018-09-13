# Emprestimo para compra de uma casa

valor_casa = float(input('Qual o valor da casa? '))
salario = float(input('Qual o valor do seu salário?'))
qtd_anos = int(input('Em quantos anos deseja pagar?'))

prestacao = valor_casa / (qtd_anos * 12)
print('Valor mensal da préstação {:.2f}'.format(prestacao))

if prestacao <= (salario * 30) / 100:
    print('Empréstimo Aprovado!')

else:
    print('Empréstimo Negado!')
