num = int(input("Digite um numero "))

print("""Escolha uma das bases para conversao:
[1] converter para BINARIO
[2] converter para OCTAL
[3] converter para HEXADECIMAL""")
opcao = int(input("Digite sua opcao: "))

def op1(numero):
    return bin(numero), "BINARIO"

def op2(numero):
    return oct(numero), "OCTAL"

def op3(numero):
    return hex(numero), "HEXADECIMAL"

def invalida(numero):
    return "Desculpe", "OPCAO INVALIDADA, TENTE NOVAMENTE"

if opcao > 3:
    opcao = 4
else:
    opcao = opcao
selecionada = {1:op1, 2:op2, 3:op3, 4:invalida}

selecionada, tipo = selecionada.get(opcao)(num)

if opcao <=3:
    print("{} convertido em {} e {} ".format(num,tipo, selecionada[2:]))
else:
    print(selecionada, tipo)