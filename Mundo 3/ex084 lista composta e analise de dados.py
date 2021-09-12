temp = []
princ = []
maior = menor = 0
while True:
    temp.append(str(input("Nome: ")))
    temp.append(float(input("Peso: ")))
    if len(princ) == 0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]
    princ.append(temp[:])
    temp.clear()
    decisao = input("Deseja continuar? ").strip().upper()
    if decisao in "N":
        break
print("-="*30)
print(f"Os dados foram {princ}")
print(f"Ao todo voce cadastrou {len(princ)} pessoas")
print(f"O maior peso foi de {maior} kg. Peso(s) de ", end = "")
for peso in princ:
    if peso[1] == maior:
        print(f"{peso[0]}", end= " e ")
print(f"\nO menor peso foi de {menor} kg. Peso(s) de ", end= "")
for peso in princ:
    if peso[1] == menor:
        print(f"{peso[0]}", end=" e ")

