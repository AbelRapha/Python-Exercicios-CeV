from random import randint

print("=-"*15)
print("Vamos jogar PAR ou IMPAR")
print("=-"*15)

vitorias_user = []
vitorias_pc = []

while(len(vitorias_pc) == 0):
    valor_user = int(input("Digite um valor "))
    opcao = input("P/I ").strip().upper()
    valor_pc = randint(0,10)
    total = valor_user + valor_pc
    if total % 2 == 0:
        if opcao == "P":
            print(f"Voce Jogou {valor_user} e o computador {valor_pc}. Total {total}\n Voce VENCEU!!\nVamos Jogar novamente..."  )
            print("=-"*15)
            valor_user = str(valor_user)
            vitorias_user.append(valor_user)
            continue
        else:
            print(f"Voce Jogou {valor_user} e o computador {valor_pc}. Total {total}\n Voce PERDEU!!" )
            print("=-"*15)
            vitorias_pc.append(valor_pc)
            break
    else:
        if opcao == "I":
            print(f"Voce Jogou {valor_user} e o computador {valor_pc}. Total {total}\n Voce VENCEU!!\n Vamos Jogar novamente..." )
            print("=-"*15)
            valor_user = str(valor_user)
            vitorias_user.append(valor_user)
            continue
        else:
            print(f"Voce Jogou {valor_user} e o computador {valor_pc}. Total {total}\n Voce PERDEU!!" )
            print("=-"*15)
            vitorias_pc.append(valor_pc)
            break
print(f"GAME OVER! Voce venceu {len(vitorias_user)} vezes")
