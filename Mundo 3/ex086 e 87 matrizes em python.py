matriz = [[0,0,0], [0,0,0], [0,0,0]]
par = soma = maior = 0
for linha in range(0,3):
    for coluna in range(0,3):
        matriz[linha][coluna] = int(input(f"Digite um valor para [{linha}, {coluna}] "))
print("-="*30)
for linha in range(0,3):
    for coluna in range(0,3):
        print(f" [{matriz[linha][coluna]:^5}]", end = "" )
        print()
        if matriz[linha][coluna] % 2 == 0:
            par += matriz[linha][coluna]

print(f"A soma dos valores pares e {par}")
for linha in range(0,3):
    soma += matriz[linha][2]
print(f"A soma dos valores da terceira coluna e {soma}")
for coluna in range(0,3):
    if coluna ==0:
        maior = matriz[1][coluna]
    elif matriz[1][coluna] > maior:
        maior = matriz[1][coluna]
print(f"O maior valor da segunda linha e {maior}")
        
