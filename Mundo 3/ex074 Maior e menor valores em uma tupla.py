from random import randint
tupla = []
for i in range(0,5):
    numRandom = randint(0,10)
    tupla.append(numRandom)
tupla = tuple(tupla)
print("A lista gerada aleatoriamente foi: ")
for n in tupla:
    print(f"{n},", end = " ")
print(f"O menor valor da lista foi {min(tupla)}\n E o maior valor {max(tupla)}")