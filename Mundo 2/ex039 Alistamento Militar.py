from datetime import date

currency_year = date.today().year

nascto = int(input("Digite o ano do seu nascimento: "))

def alistamento(nascto, currency_year):
    idade = currency_year - nascto
    if idade == 18:
        return f"Voce tem {idade} anos, chegou a hora do seu alistamento"
    elif idade > 18:
        ano_alistamento = idade - 18
        anoExato = currency_year - ano_alistamento
        return f"Voce tem {idade} anos, e o seu alistamento foi ha {ano_alistamento} ano(s) atras em , {anoExato} "
    else:
        ano_alistamento = 18 - idade
        anoExato = currency_year + ano_alistamento
        return f"Voce tem {idade} anos, e o seu alistamento sera daqui {ano_alistamento} ano(s). Mais precisamente no ano de {anoExato}"

print(alistamento(nascto, currency_year))