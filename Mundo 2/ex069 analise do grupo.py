lista_homens = []
lista_mulheres20 = []
totMais18 = 0

decisao = ""
while("N" not in decisao):
    print("-*"*15)
    print("CADASTRO DE PESSOAS")
    print("-*"*15)

    idade = int(input("Idade: "))
    sexo = input("Sexo [M/F] ").strip().upper()
    if sexo in "M":
        lista_homens.append(sexo)
    else:
        if idade < 20:
            idade = str(idade)
            lista_mulheres20.append(idade)
        else:
            continue
    idade = int(idade)
    if idade > 18:
        totMais18 +=1
    decisao = input("Quer Continuar? ").strip().upper()

print(f"Ha ao todo {totMais18} pessoas com mais de 18 anos. E ao todo foram {len(lista_homens)} homens cadastrados \n e {len(lista_mulheres20)} mulheres abaixo dos 20 anos. ")
print("Obrigado e Volte Sempre!! ")