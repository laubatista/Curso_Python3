'''Aprimore o desafio 93 para que ele funcione com vários jogadores, incluido um sistema
de visualição de detalhes do aproveitamento de cada joogador'''

relatorio = dict()
desempenho = list()
time = list()
while True:
    relatorio.clear()
    relatorio['nome'] = str(input('Nome do Jogador:'))
    partidas = int(input(f'Quantas partidas {relatorio["nome"]} jogou?'))
    desempenho.clear()
    for c in range(1, partidas+1):
        desempenho.append(int(input(f'Quantos gols na partida {c}?')))
    relatorio['gols'] = desempenho[:]
    relatorio['total'] = sum(desempenho)
    time.append(relatorio.copy())
    while True:
        resp = str(input('Quer continuar? [S/N]')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break

print('-'* 30)
print('cod ', end='')
for i in relatorio.keys():
    print(f' {i:<15}', end='')
print()
print('-' * 40)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 40)
while True:
    busca = int(input('Mostrar dados de qual jogador? [999 para parar]'))
    if busca == 999:
        break
    if busca >= len(time):
        print(f' ERRO! Não exixte jogador cm o código {busca}!')
    else:
        print(f'  -- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}:')
        for i, g in enumerate(time[busca]['gols']):
            print(f'     No jogo {i+1} fez {g} gols.')
        print('-'* 40)
print('<<< VOLTE SEMPRE >>>')