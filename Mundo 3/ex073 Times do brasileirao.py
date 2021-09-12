brasileirão = ('Palmeiras', 'Flamengo', 'Internacional', 'Grêmio', 'São Paulo',
    'Atlético Mineiro', 'Atlético-PR', 'Cruzeiro', 'Botafogo', 'Santos',
    'Bahia', 'Corinthians', 'Fluminense', 'Ceará', 'Vasco da Gama', 'Sport Recife',
    'América-MG', 'Chapecoense', 'Vitória', 'Paraná')
print(f"Os 5 primeiros da lista {brasileirão[:5]} ")
print("-="*30)
print(f" O 4 ultimos colocados {brasileirão[-4:]}")
print("-="*30)
print(f" Time em ordem alfabetica {sorted(brasileirão)}")
print("-="*30)
print(f"A posicao em que a chapecoense se encontra e {brasileirão.index('Chapecoense')+1}")
print("-="*30)