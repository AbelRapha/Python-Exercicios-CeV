tabuada = int(input("Digite o numero da tabuada que deseja calcular: "))

print("-"*15)
for i in range(1,11,1):
    print(f"{tabuada:2} x {i:2} = {tabuada*i}")

print("-"*15)  