from abc import abstractproperty


lista = []
listaPares =[]
listaImpares = []
while True:
    num = int(input("Digite um valor: "))
    lista.append(num)
    if num % 2 ==0:
        listaPares.append(num)
    else:
        listaImpares.append(num)
    decisao = input("Quer continuar? ").strip().upper()
    if decisao in "N":
        break
    else:
        continue
print(f"Lista de numeros digitados {lista} ")
print(f"Lista de numeros pares {listaPares}")
print(f"lista de numeros impares {listaImpares}")

