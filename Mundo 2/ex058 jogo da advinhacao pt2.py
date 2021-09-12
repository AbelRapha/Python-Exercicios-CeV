import time
import random

print("Acabei de pensar em um numero entre 0 e 10.\n Sera que consegue adivinhar?")
palpite = int(input("Qual o seu palpite? "))
escolha_pc = random.randint(0,10)
tentativas = 0
while(palpite != escolha_pc):
    if palpite > escolha_pc:
        print("Menos... Tente mais uma vez.")
        palpite = int(input("Qual o seu palpite? "))
    else:
        print("Mais... Tente mais uma vez.")
        palpite = int(input("Qual o seu palpite? "))
    tentativas +=1
print(f"Parabens voce acertou! Total de tentativas {tentativas}")