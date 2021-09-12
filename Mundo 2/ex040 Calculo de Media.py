n1 = float(input("Digite sua primeira nota: "))
n2 = float(input("Digite sua segunda nota: "))

def media(n1,n2):
    media = (n1+n2)/2
    if media < 5:
        return f"REPROVADO, SUA MEDIA FOI DE {media:.1f}"
    elif media >= 5 and media < 7:
        return f"RECUPERACAO, SUA MEDIA FOI DE {media:.1f}"
    else:
        return f"APROVADO! Sua media foi de {media:.1f}"

print(media(n1,n2))