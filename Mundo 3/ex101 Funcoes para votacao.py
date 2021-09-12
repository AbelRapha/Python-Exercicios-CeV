from datetime import date

def anoVoto(ano):
    idade = date.today().year - ano
    if idade < 16:
        return f"Com {idade} anos: Nao Vota"
    elif 16<idade<18:
        return f"Com {idade} anos: Voto Opcional"
    else:
        return f"Com {idade} anos: Voto Obrigatorio"

print("-"*30)
anoNascto = int(input("Em que ano voce nasceu? "))
print(anoVoto(anoNascto))