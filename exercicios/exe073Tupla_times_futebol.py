''' Criar uma tupla com os 20 primeiros colocados na tabela do brasileirão, na ordem de colocação.
    A - Mostrar os 5 primeiros colocados
    B - Os últimos 4 colocados
    C - Listar os times em ordem alfabética
    D - Mostrar em qual posição o time da Chapecoense está na tabela. '''



times = ('Palmeira', 'Santos', 'Atlético', 'Botafogo', 'Flamengo', 'Bahia', 'Internacional', 'São Paulo',
          'Goiás', 'Corinthias','Athletico-PR', 'Ceará', 'Grêmio', 'Cruzeiro','Fluminense', 'Chapecoense',
          'Fortaleza', 'Vasco', 'CSA', 'Avaí')


print(f'Lista de times do Brasileirão:')
for t in times:
    print(t)


print(f'Os 5 primeiros colocados são:\n {times[0:5]}')

print(f'Os 4 últimos colocados são:\n {times[-4:]}')

print(f'Times em ordem alfabética\n {sorted(times)}')

print(f'O chapecoense está na {times.index("Chapecoense")+1} posicao')
