from datetime import datetime
dicTrabalhadores = dict()
print("-="*30)
dicTrabalhadores["nome"] = input("Nome: ").strip()
nascimento = int(input("Ano de nascimento: "))
dicTrabalhadores["idade"] = datetime.now().year - nascimento
dicTrabalhadores["carteira_de_trabalho"] = int(input("Digite o numero da sua carteira de trabalho (Digite 0 se nao tem) "))

if dicTrabalhadores["carteira_de_trabalho"] == 0:
    
    for k,v in dicTrabalhadores.items():
        print(f'{k} {v}')
else:
    
    dicTrabalhadores["ano_contratacao"] = int(input("Digite o ano da sua contratacao: "))
    dicTrabalhadores["salario"] = float(input("Digite o seu salario: "))
    dicTrabalhadores["aposentadoria"] = ((dicTrabalhadores["ano_contratacao"] + 35) - datetime.now().year)
    for k,v in dicTrabalhadores.items():
        print(f'{k} {v}')
print("-="*30)


