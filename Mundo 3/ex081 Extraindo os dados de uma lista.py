lista = []
while True:
    lista.append(int(input("Digite um numero: ")))
    decisao = input("Quer continuar? ").strip()
    if decisao in "Nn":
        break

print(f"Voce digitou {len(lista)} elemento(s)")
print(f"Os valores em ordem decrescente {sorted(lista, reverse= True)}")
print(f"O valor 5 ", end = "")
if 5 in lista:
    print("Foi encontrado na lista")
else:
    print("Nao foi encontrado na lista")