from datetime import date
maioridade = 0
menoridade = 0
for count in range(1,8):
    nascto = int(input("Digite o ano do seu nascimento: "))
    ano_atual = date.today().year
    if ano_atual - nascto > 18:
        maioridade +=1
    else:
        menoridade += 1
print(f"Ha ao todo ha {maioridade} pessoas maiores de idade e {menoridade} menores de idade")    