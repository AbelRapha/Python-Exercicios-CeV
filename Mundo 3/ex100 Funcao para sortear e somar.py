from random import randint
from time import sleep

def somaPar(lista):
    print("Somando os valores pares de {}".format(lista), end= '')
    parSoma = 0
    for i,v in enumerate(lista):
        if v%2==0:
            parSoma +=v
    print("Temos {}".format(parSoma))

def sorteio(lista):
    print("Sorteando 5 valores da lista: ", end= "")
    i = 0
    while(len(lista) <5):
        valor_sorteado = randint(1,10)
        if i ==0:
            lista.append(valor_sorteado)
            i+=1
            print(f'{valor_sorteado}', end= ' ', flush= True)
            sleep(0.3)
        else:
            if valor_sorteado in lista:
                continue
            else:
                lista.append(valor_sorteado)
                print(f'{valor_sorteado}', end= ' ', flush= True)
                sleep(0.3)

lista = []
sorteio(lista=lista)
print()
somaPar(lista=lista)
