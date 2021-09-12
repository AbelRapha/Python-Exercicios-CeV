print("="*20)
print("10 TERMOS DE UMA PA")
print("="*20)

valor = float(input(f"Digite o 1º termo: "))
razao = float(input("Digite a razao da PA "))

print(valor)
for cont in range(1,10):
    print(valor+(razao*cont), "...", end="")
