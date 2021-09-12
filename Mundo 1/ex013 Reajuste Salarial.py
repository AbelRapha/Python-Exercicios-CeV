salario = float(input("Digite o seu salario "))

def reajusteSalarial(salario):
    return salario + salario*15/100

print(f"O seu novo salario com o reajuste de  15% sera de  R$ {reajusteSalarial(salario):.2f}")