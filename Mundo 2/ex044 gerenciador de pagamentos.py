preco = float(input("Digite um preco "))

print("""Escolha a forma de pagamento:
[1] a vista dinheiro/cheque
[2] a vista no cartao
[3] em ate 2x no cartao de credito"
[4] 3x ou mais no cartao""")

opcao = int(input("Digite sua opcao: "))

def AvistaOuChque(preco):
    return preco - preco*10/100, "10% DE DESCONTO"

def AvistaCartao(preco):
    return preco - preco*5/100, "5% DE DESCONTO"

def Ate2xCartao(preco):
    return preco, "SEM DESCONTO"

def Em3xOuMais(preco):
    return preco + preco*30/100, "Juros de 30%"

def invalida(preco):
    return "Desculpe", "OPCAO INVALIDADA, TENTE NOVAMENTE"

if opcao > 4:
    opcao = 5
else:
    opcao = opcao

selecionada = {1:AvistaOuChque, 2:AvistaCartao, 3:Ate2xCartao, 4:Em3xOuMais, 5:invalida}

selecionada, tipo = selecionada.get(opcao)(preco)

if opcao <=4:
    print("O valor da sua compra sera de R$ {:.2f} {} ".format(selecionada, tipo))
else:
    print(selecionada, tipo)