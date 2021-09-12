from time import sleep

valor1 = float(input("Digite um valor "))
valor2 = float(input("Digite um outro valor "))

print("""""O que deseja fazer com esses valores?
[1] somar
[2] Multiplicar
[3] Descobrir quem e Maior
[4] novos valores
[5] Sair do programa""""")
opcao = int(input())

def soma(a,b):
    return a+b

def multiplica(a,b):
    return a*b

def maiorValor(a,b):
    if a>b:
        return a
    elif a==b:
        return "Nao ha, pois Sao Iguais"
    else:
        return b


while(opcao != 5):
    if opcao == 1:
        print("A soma entre {} e {} e {}".format(valor1,valor2,soma(valor1,valor2)))
                
    elif opcao == 2:
        print("A multiplicacao entre {} e {} e {}".format(valor1,valor2,multiplica(valor1,valor2)))

    elif opcao ==3:
        print("O maior valor entre {} e {}, {}".format(valor1,valor2,maiorValor(valor1,valor2)))
    elif opcao == 4:
        valor1 = float(input("Digite um valor "))
        valor2 = float(input("Digite um outro valor "))
    else:
        print("Opcao invalida. \n Digite outra opcao")
    print("-=="*20)    
    print("""                 [1] somar
                 [2] Multiplicar
                 [3] Descobrir quem e Maior
                 [4] novos valores
                 [5] Sair do programa""""")
    opcao = int(input())    
        
    
print("Finalizando...")
sleep(2)
print("Fim do programa! Volte Sempre.")
