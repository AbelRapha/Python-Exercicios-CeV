lista = []
maior = 0
menor = 0
for item in range(0,5):
    lista.append(int(input(f"Digite um valor para a posicao {item+1}: ")))
    if item == 0:
        maior = menor = lista[item]
    else:
        if lista[item] > maior:
            maior = lista[item]
        if lista[item] < menor:
            menor = lista[item]
print(f"Voce digitou os valores {lista}")
print(f"O maior valor digitado foi {max(lista)} na(s) posicoes ", end = '')
for i,v in enumerate(lista):
    if v == maior:
        print(f"{i}...", end = " ")
print()

print(f"O menor valor digitado foi {min(lista)} na(s) posicoes ", end = "")
for i,v in enumerate(lista):
    if v == menor:
        print(f"{i}...", end = " ")
