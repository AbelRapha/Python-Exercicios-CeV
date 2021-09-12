from time import sleep

def cont(i,f,p):
    if i < f:
        print(f"A contage de {i} ate {f} de {p} em {p}:")
        for cont in range(i,f+1,p):
            print(cont, end = ' ')
            sleep(0.5)
    else:
        print(f"A contage de {i} ate {f} de {p} em {p}:")
        for cont in range(i,f+1,-p):
            print(cont, end = ' ')
            sleep(0.5)
    print("FIM!")

cont(1,10,1)
cont(10,0,2)
print("Agora e a sua vez de personalizar a contagem")
i = int(input("Inicio: "))
f = int(input("Final: "))
p = int(input("Passo: "))
print(cont(i,f,p))
