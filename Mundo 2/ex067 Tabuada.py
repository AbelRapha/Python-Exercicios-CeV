n = 1
while(n > 0):
    tabuada = int(input("Digite o numero da tabuada que deseja calcular: "))
    if tabuada > 0:
        print("-"*15)
        for i in range(1,11,1):
            print(f"{tabuada:2} x {i:2} = {tabuada*i}")

        print("-"*15)
        continue
    else:
        break
print("Programa encerrado! Volte sempre")