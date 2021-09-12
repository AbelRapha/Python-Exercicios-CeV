kmRodados = float(input("Quantos km voce rodou? "))
diasAlugados = int(input("Por quantos dias voce alugou ele? "))

def aluguel(km,dia):
    return 60*dia + km*0.15
print(f"O valor a se pagar nesse alguel sera de R$ {aluguel(kmRodados, diasAlugados):.2f}")    