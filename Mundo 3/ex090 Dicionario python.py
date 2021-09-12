alunos = {}
alunos["nome"] = input("Nome: ").strip()
alunos["media"] = float(input(f'Media do {alunos["nome"]}: '))
if alunos["media"] > 6:
    alunos["situacao"] = "APROVADO"
elif 5 < alunos["media"] < 6:
    alunos["situacao"] = "RECUPERACAO"
else: 
    alunos["situacao"] = "REPROVADO"
print("-="*30)
for k, v in alunos.items():
    print(f' - {k} e igual a {v}')