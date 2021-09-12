from typing import ChainMap


n1 = int(input("Digite o primeiro valor: "))
n2 = int(input("Digite o segundo valor: "))
n3 = int(input("Digite o terceiro valor: "))

def comparar(n1,n2,n3):
    if n1 > n2 and n1 > n3:
        maior_valor = n1
        if n2>n3:
            menor_valor = n3
        else:
            menor_valor = n2
    elif n2>n1 and n2>n3:
        maior_valor = n2
        if n1>n3:
            menor_valor = n3
        else:
            menor_valor = n1
    else:
        maior_valor = n3
        if n2>n1:
            menor_valor = n1
        else:
            menor_valor = n2
    return maior_valor, menor_valor

maior_valor, menor_valor = comparar(n1,n2,n3)

print(f"O maior valor digitado {maior_valor}\n O menor valor digitado {menor_valor}")
