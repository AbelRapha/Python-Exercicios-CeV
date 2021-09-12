decisao = " "
listanum = []
while decisao not in "N":
    num = (int(input("Digite um valor: ")))
    if num not in listanum:
        listanum.append(num)
        print("Valor adicionado com Sucesso")
    else:
        print("Este valor ja foi inserido ")
    decisao = input("Deseja continuar? ").strip().upper()
print(f"A lista de valores cadastrado foi {sorted(listanum)}")    
print("Obrigado e Volte sempre")

