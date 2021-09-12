expressao = str(input("Digite a expressao: "))
pilha = []
for simbolo in expressao:
    if simbolo == "(":
        pilha.append("(")
    elif simbolo == ")":
        if len(pilha) > 0:
            pilha.pop()#remove o ultimo elemento da lista
        else:
            pilha.append(")")
            break
if len(pilha) == 0:
    print("Sua expressao esta valida")
else:
    print("Sua expressao nao esta valida")