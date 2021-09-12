import time
import random

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

print("--="*20)
numero = int(input("Digite um numero entre 0 e 5 "))

numeroDaMaquina = random.randint(0,5)

time.sleep(1)
print(bcolors.OKBLUE+"Processando")
time.sleep(3)
if numero == numeroDaMaquina:
    print(bcolors.OKGREEN+ f"Parabens voce acertou! O numero que tinha escolhido era o {numeroDaMaquina}")
else:
    print(bcolors.FAIL+ f"Voce Perdeu. O numero que eu havia pensado era o {numeroDaMaquina}")
print("--="*20)    
