salario = float(input("Digite o seu salario "))

def aumentoSalario(salario):
    if salario > 1250.0:
        aumento = salario + salario*10/100
    else:
        aumento = salario + salario*15/100
    return aumento


print(f"O seu novo salario reajustado sera de R$ {aumentoSalario(salario)}")    