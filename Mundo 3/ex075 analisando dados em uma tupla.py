tupla = []
for i in range(0,4):
    num = int(input(f"Digite o {i+1}º valor "))
    tupla.append(num)

tupla = tuple(i for i in tupla)

print(f"O valor 9 foi digitado {tupla.count(9)} vez(es)")
if 3 in tupla:
    print(f"O numero 3 apareceu {tupla.index(3)} vez(es)")
else:
    print("Nao foi digitado nenhum valor 3")
print(f"Sequencia de numeros pares: ", end = "")
for n in tupla:
    if n % 2 ==0:
        print("  ➡  ",n, end = " ")