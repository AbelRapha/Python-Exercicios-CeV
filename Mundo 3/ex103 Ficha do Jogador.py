print("-"*30)
nome = input("Nome do Jogador: ").strip()
gols = input("NUmero de gols: ").strip()
def ficha(nome,gols):
    if gols.isnumeric():
        if nome == '':
            return f'O jogador <desconhecido> fez {gols} gols(s) no campeaonato'
        else:
            return f'O jogador {nome} fez {gols} gol(s) no campeonato'
    else:
        if nome ==  '':
            return f'O jogador <desconhecido> fez 0 gol(s) no campeaonato'
        else:
            return f'O jogador {nome} fez 0 gol(s) no campeonato'
print(ficha(nome,gols))