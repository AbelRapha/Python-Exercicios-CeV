dictJogador = dict()
gols = list()
jogadores = []
#Validacao dos dados
while True:
    dictJogador.clear()
    gols.clear()
    dictJogador["Nome"] = input("Nome do jogador: ").strip()
    partidas = int(input(f'Quantas partidas {dictJogador["Nome"]} jogou?  '))
    for c in range(0,partidas):
        gols.append(int(input(f'Quantos gols na {c+1}ª? ')))
    dictJogador['Gols'] = gols[:]
    totalGols = sum(gols)
    dictJogador["Total"] = totalGols
    jogadores.append(dictJogador.copy())
    while True:
        resp = input("Deseja Continuar? [S/N] ").strip()
        if resp in "nNSs":
            break
        print("Erro! Responda apenas S ou N")
    if resp in "Nn":
        break
#Apresentacao dos resultados
print("-="*40)
print('Cod', end='')
for i in dictJogador.keys():
    print(f'{i:<15}', end = '')
print()
print("-"*40)
for k,v in enumerate(jogadores):
    print(f'{k:>5} ', end = '') 
    for d in v.values():
        print(f'{str(d):<15}', end = '')
    print()
print("-="*40)
#Busca dos dados
while True:
    busca = int(input("Mostrar dados de qual jogador? (Digite 999 para sair do programa) "))
    if busca == 999:
        break
    if busca >= len(jogadores):
        print(f"ERRO Nao existe jogador com codigo {busca}")
    else:
        print(f' --> Levantamento do Jogador {jogadores[busca]["Nome"]}: ')
        for i,v in enumerate(jogadores[busca]['Gols']):
            print(f'Na partida {i+1}, fez {v} gols')
            print(f'Foi um total de {jogadores[busca]["Total"]} gols')
        print('-'*40)
print("Volte Sempre! ")