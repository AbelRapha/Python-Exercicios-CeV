listagem = ("lapis", 1.70, "borracha", 3.0, "Caderno", 5.0, "Estojo", 3.5)
print("-"*40)
print(f"{'LISTAGEM DE PRECOS':^40}")  
print("-"*40)
for posicao in range(0, len(listagem)):
    if posicao % 2==0:
       print(f"{listagem[posicao]:<30}", end = " ")
    else:
        print(f"R$ {listagem[posicao]:>7.2f}") 
print("-"*40)