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

numero = int(input(bcolors.OKBLUE+ "Digite um numero "))


if numero % 2 == 0:
    print("O numero e Par")
else:
    print("O numero e Impar")    