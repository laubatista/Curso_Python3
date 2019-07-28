'''Crie um programa que gerêncie o aproveitamento de um jogador de futebool.
O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a
quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluido o total
de gols feitos durante o campeonato'''

relatorio = dict()
desempenho = list()

relatorio['nome'] = str(input('Nome do Jogador:'))
partidas = int(input(f'Quantas partidas {relatorio["nome"]} jogou?'))
total = 0
for c in range(1, partidas+1):
    desempenho.append(int(input(f'Quantos gols na partida {c}?')))
relatorio['gols'] = desempenho[:]
relatorio['total'] = sum(desempenho)

print('-=' * 30)
print(relatorio)
print('-='* 30)
for k, v in relatorio.items():
    print(f'O campo {k} têm valor {v}.')

print('-='*30)
print(f'O jogador {relatorio["nome"]} jogou {len(relatorio["gols"])} partidas.')
for i, v in enumerate(relatorio["gols"]):
    print(f'   => Na partida {i}, Fez {v} gols ')

print(f'Foi um total de {relatorio["total"]} gols')
