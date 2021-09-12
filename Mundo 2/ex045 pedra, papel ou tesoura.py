from random import randint
from time import sleep

print("Escolha sua opcao:\n[0] PEDRA\n[1] PAPEL\n[2] TESOURA")

opcao = int(input())
sleep(1)
print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PO!!!")
print("-="*20)
def jokenpo(user):
    opcao_usuario = user
    opcao_pc = randint(0,2)
    opcoes = {0: 'pedra', 1: "papel", 2:'tesoura'}
    escolha_pc = opcoes.get(opcao_pc)
    escolha_usuario = opcoes.get(opcao_usuario)

    if str(escolha_pc) == str(escolha_usuario):
        return f"Empate! Computador jogou {escolha_pc} e Jogador jogou {escolha_usuario}" 
    elif escolha_usuario == "tesoura" and escolha_pc == "pedra":
        return f"COMPUTADOR VENCEU! Computador jogou {escolha_pc} e jogador jogou {escolha_usuario}"
    elif escolha_usuario == "pedra" and escolha_pc == "tesoura":
        return f"JOGADOR VENCEU! Computador jogou {escolha_pc} e jogador jogou {escolha_usuario}"
    elif escolha_usuario == "tesoura" and escolha_pc == "papel":
        return f"JOGADOR VENCEU! Computador jogou {escolha_pc} e jogador jogou {escolha_usuario}"
    elif escolha_usuario == "papel" and escolha_pc == "tesoura":
        return f"COMPUTADOR VENCEU! Computador jogou {escolha_pc} e jogador jogou {escolha_usuario}"
    elif escolha_usuario == "papel" and escolha_pc == "pedra":
        return f"JOGADOR VENCEU! Computador jogou {escolha_pc} e jogador jogou {escolha_usuario}"
    elif escolha_usuario == "pedra" and escolha_pc == "papel":
        return f"COMPUTADOR VENCEU! Computador jogou {escolha_pc} e jogador jogou {escolha_usuario}"
    else:
        return "OPCAO INVALIDA TENTE NOVAMENTE"

print(jokenpo(opcao))    
print("-="*20)
