num = int(input("Digite um numero:"))
num2 = int(input("Digite um outro numero:"))

def comparar(n1,n2):
    if n1 == n2: 
        return "Nao existe valor maior. Os dois numeros sao iguais"
    elif n1 > n2:
        return f" {n1} e maior que {n2}"
    else: 
        return f"{n2} e maior que {n1}"

print(comparar(num, num2))