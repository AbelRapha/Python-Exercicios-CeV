preco = float(input("Digite um preco "))

def off5(preco):
    return preco - preco*5/100

print(f"O valor do produto com o desconto aplicado sera de R$ {off5(preco):.2f}")