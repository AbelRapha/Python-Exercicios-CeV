cont = ("zero","um","dois","três", "quatro","cinco","seis","sete","oito","nove",
"dez", "onze","doze","treze","quatorze","quinze","dezesseis","dezessete","dezoito",
"dezenove","vinte")
decisao = " "
while decisao not in "N":
    num = int(input("Digite um numero entre 0 e 20: "))
    if 0<= num <= 20:
        print(f"Voce digitou o numero {cont[num]}")
        decisao = input("Deseja continuar? ").strip().upper()
    else:
        print("Tente novamente. ", end = "")
        continue
print("Obrigado e volte sempre!")