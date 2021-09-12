nota1 = int(input("Digite aqui a sua primeira nota "))
nota2 = int(input("Digite aqui a sua segunda nota "))

def Media(n1,n2):
    return (n1+n2) /2

print(f"Considerando as notas inseridas a sua media final foi {Media(nota1,nota2):.2f}")