
decisao = " "
while(decisao not in "N"):
    palavras = tuple(str(input(f"Digite a {i}ª Palavra ")).strip().lower() for i in range(1,5))
    for p in palavras:
        print(f"\n Na palavra {p} temos ", end = '')
        for letra in p:
            if letra in "aeiou":
                print(letra, end = ' ')
    decisao = input("\n Quer continuar? ").strip().upper()

print("Obrigado e volte sempre!")