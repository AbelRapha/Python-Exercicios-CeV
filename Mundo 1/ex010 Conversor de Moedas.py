money = float(input("Quanto voce possui em carteira? "))

def cambio(money):
    return money/5.2

print(f"Com R$ {money:.2f} e possivel comprar $ {cambio(money):.2f}")