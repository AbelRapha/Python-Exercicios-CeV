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

num = int(input("Digite um numero: "))

quantidadeDivisoes = 0
for count in range(1,num+1):
    if num % count == 0:
        print('\033[92m', end = " ")
        quantidadeDivisoes += 1
    else:
        print('\033[93m', end = " ")
    print("{}".format(count), end = " ")

if quantidadeDivisoes <=2:
    print('\n\033 O numero {} foi divisivel {} vezes. \n E por isso ele E PRIMO!'.format(num, quantidadeDivisoes))
else:
    print('\n\033 O numero {} foi divisivel {} vezes. \n E por isso ele NAO E PRIMO!'.format(num,quantidadeDivisoes))