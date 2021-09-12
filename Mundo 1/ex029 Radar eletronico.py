velocidade = int(input("Digite o valor da velocidade "))

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

custo = (velocidade - 80)*7    

if velocidade > 80:
    print(bcolors.WARNING+ f"Voce foi multado. A multa aplicada foi de R$ {custo}")
else:
    print(bcolors.OKGREEN+ f"Voce esta dentro do limite de velocidade da via")