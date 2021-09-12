valor = float(input(f"Digite o 1º termo: "))
razao = float(input("Digite a razao da PA "))
n = 1
cont = 1
total = 0
maisTermos = 10
while(maisTermos != 0 ):
    total += maisTermos
    while(cont <= total):
        print(valor, end= '  ➡  ')
        valor += razao
        cont +=1
    print("Pausa") 
    maisTermos = int(input("Quantos termos voce quer mostrar a mais? "))
print("Fim")
print("No total foram {} somas".format(total))