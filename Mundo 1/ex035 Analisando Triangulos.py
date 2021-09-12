print("-="*20)
print("Analisador de Triangulos")

lado1 = int(input("Digite o primeiro lado "))
lado2 = int(input("Digite o segundo lado "))
lado3 = int(input("Digite o terceiro lado "))


def existTriangle(l1,l2,l3):
    if l1 < l2+l3 and l1 > abs(l2-l3):
        if l2 < l1+l3 and l2 > abs(l1-l3):
            if l3 < l2+l1 and l3 > abs(l2-l1):
                return "PODEM FORMAR"
    else:
        return "NAO PODEM FORMAR"


print("Os segmentos acima {} triangulo!".format(existTriangle(lado1,lado2,lado3)))

print("-="*20)