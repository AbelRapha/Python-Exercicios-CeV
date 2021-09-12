from datetime import date

ano = int(input("Digite o Ano. Ou coloque 0 para analisar o ano atual "))

if ano ==0:
    ano = date.today().year

if ano % 4 ==0 and ano % 100 != 0 or ano % 400 ==0:
    print("O ano {}  e Bissexto". format(ano))
else:
    print("O ano {} nao e Bissexto".format(ano))