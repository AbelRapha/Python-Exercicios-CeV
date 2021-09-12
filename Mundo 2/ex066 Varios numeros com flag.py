n = 0
lista_numeros = []
while(n != 999):
    n = int(input("Digite um numero [ou digite 999 para parar] "))
    if n!= 999:
        n = str(n)
        lista_numeros.append(n)
    else:
        break
for item in range(0, len(lista_numeros)):
    lista_numeros[item] = int(lista_numeros[item])
print("A soma dos {} valores digitados anteriormente foi {}". format(len(lista_numeros),sum(lista_numeros)))
