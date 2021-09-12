idade = int(input("Digite sua idade "))

def classificacao(idade):
    if idade <= 9:
        return f"Um atleta de {idade} anos e Atleta MIRIM"
    elif idade > 9 and idade <=14:
        return f"Um atleta de {idade} anos e Atleta Infantil"
    elif idade > 14 and idade <= 19:
        return f"Um atleta de {idade} anos e Atleta Junior"
    elif idade > 19  and idade <= 25:
        return f"Um atleta de {idade} anos e Atleta Senior"
    else:
        return f"Um atleta de {idade} anos e Atleta MASTER"

print(classificacao(idade))