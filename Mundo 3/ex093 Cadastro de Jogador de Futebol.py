dictJogador = dict()
dictJogador["Nome"] = input("Nome do jogador: ").strip()
partidas = int(input(f'Quantas partidas {dictJogador["Nome"]} jogou?  '))
gols = list()
for c in range(0,partidas):
    gols.append(int(input(f'Quantos gols na {c+1}ª? ')))
dictJogador['Gols por partida'] = gols[:]
totalGols = sum(gols)
dictJogador["Total de gols"] = totalGols
print(dictJogador)
print("-="*30)
for k, v in dictJogador.items():
    print(f'O campo {k} tem valor {v}')
print("-="*30)
print(f'O jogador {dictJogador["Nome"]} jogou {partidas} partidas')
for i,v in enumerate(dictJogador['Gols por partida']):
    print(f'Na partida {i+1}, fez {v} gols')
print(f'Foi um total de {totalGols} gols')