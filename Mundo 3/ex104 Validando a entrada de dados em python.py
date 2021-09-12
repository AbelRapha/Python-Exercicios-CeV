n = input("Digite um numero: ")
def leiaInt(n):
    while True:
        if n.isnumeric():
            print(f"Voce acabou de digitar o numero {n} ")
            break
        else:
            print("\033[0;31mERRO! Digite um numero inteiro valido.\033[0;31m ")
            n = input("\033[1;97mDigite um numero:\033[1;97m ")
leiaInt(n)