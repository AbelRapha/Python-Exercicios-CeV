from random import sample, randint
from time import sleep

apostas = int(input("Quantas apostas deseja realizar? "))
jogos = []
while apostas:
    lista=[]
    while len(lista)<=6:
        num = randint(1,60)
        if num not in lista:
            lista.append(num)
    lista.sort()
    jogos = lista.copy()
    print(jogos)
    apostas -= 1
    jogos.clear()
    sleep(1)
print("Boa sorte")


        
