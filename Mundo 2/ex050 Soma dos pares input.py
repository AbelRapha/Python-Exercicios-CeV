soma = 0
contagem = 0
for count in range(1,7):
    print(f"Digite o {count}º valor")
    valor = int(input())
    if valor % 2 ==0:
        soma += valor
        contagem += 1
print(f"Voce informou um total de {contagem} numeros pares e a soma deles foi {soma}")