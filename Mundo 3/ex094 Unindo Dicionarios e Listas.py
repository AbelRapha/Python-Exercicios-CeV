dictCadastro = dict()
galera = []
media = soma = 0
while True:
    dictCadastro.clear()
    dictCadastro["nome"] = input("Nome: ").strip()
    dictCadastro["sexo"] = input("Sexo: [M/F] " ).strip()[0]
    while dictCadastro["sexo"] not in "MmFf":
        print("ERRO! Por favor, digite apenas M ou F ")
        dictCadastro["sexo"] = input("Sexo [M/F] ")
    dictCadastro["idade"] = int(input("Idade: "))
    soma += dictCadastro["idade"]
    galera.append(dictCadastro.copy())
    resp = input("Quer continuar? [S/N] ").strip()
    while resp not in "sSnN":
        print("ERRO! Responda apenas S ou N")
        resp = input("Quer continuar? [S/N] ")
    if resp in "nN":
        break       
print(f"Ha ao todo {len(galera)} pessoas cadastradas")
media = soma / len(galera)
print(f"A media de idade e de {media:5.2f} anos")
print("As mulheres cadastradas foram ", end = "")
for p in galera:
    if p["sexo"] in "fF":
        print(f'{p["nome"]}', end= "")
for p in galera:
    if p["idade"] >= media:
        print("   ")
        for k, v in p.items():
            print(f'{k} = {v} ', end = '')
            print()
print("ENCERRADO")
