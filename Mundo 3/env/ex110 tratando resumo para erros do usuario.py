from funcoes import resumo,leiadinheiro

valor = input("Digite um valor: R$").strip().replace(',','.')
valor = leiadinheiro(palavra=valor)
aumento = int(input(f"Digite quantos % de aumento deseja: "))
desconto = int(input(f"Digite quantos % de aumento deseja: "))
print(resumo(valor,aumento,desconto))