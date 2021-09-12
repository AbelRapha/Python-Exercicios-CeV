print("="*20)
print("10 TERMOS DE UMA PA")
print("="*20)

valor = float(input(f"Digite o 1º termo: "))
razao = float(input("Digite a razao da PA "))
n = 0
while(n <= 10):
    print(valor, end= '  ➡  ')
    valor += razao
    n +=1
print("Fim")    