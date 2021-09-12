import time

valorCasa = float(input("Digite o valor da Casa que deseja adquirir: "))
salario = float(input("Digite o seu salario: "))
anos = int(input("Em quantos voce quer pagar esse financiamento? "))
prestacao = valorCasa/ (12*anos)

def aprovacaoEmprestimo(prestacao, salario):
    if prestacao <= 0.3*salario:
        return "APROVADO"
    else:
        return "REPROVADO"

print("Para pagar uma casa no valor de R$ {:,.2f} em {} anos a prestacao sera de R$ {:,.2f} por mes.".format(valorCasa,anos, prestacao))
print("Analisando a aprovacao do financiamento. Aguarde... ")
time.sleep(3)
print(aprovacaoEmprestimo(prestacao,salario))