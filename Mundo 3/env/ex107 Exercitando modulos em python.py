import funcoes
p = float(input("Digite o preco: R$ "))
print(f"a metade de {p} e R$ {funcoes.metade(p)}")
print(f'O dobro de {p} e R$ {funcoes.dobro(p)}')
print(f"Aumentando 10%, temos R$ {funcoes.aumentar(p,10)}")
print(f'Reduzindo 13% temos R$ {funcoes.diminuir(p,13)}')