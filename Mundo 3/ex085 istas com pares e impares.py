listanum = [[],[]] #Primeiro colchete numeros pares e segundo colchete numeros impares
valor = 0
for cont in range(1,8):
    valor = int(input("Digite um valor: "))
    if valor % 2 ==0:
        listanum[0].append(valor)
    else:
        listanum[1].append(valor)
listanum[0].sort()
listanum[1].sort()
print(f"Os numeros pares digitados foram {listanum[0]}")
print(f"Os numeros impares digitados foram {listanum[1]}")

