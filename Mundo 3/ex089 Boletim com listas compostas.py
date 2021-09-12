alunosNotas = []

while True:
    nome = input("Nome: ").strip()
    nota1 = float(input("Digite a nota da P1: "))
    nota2 = float(input("Digite a nota da P2:  "))
    media = (nota1 + nota2)/2
    if media > 6:
        situacao = "APROVADO"
    elif 5 < media < 6:
        situacao = "RECUPERACAO"
    else:
        situacao = "REPROVADO"
    alunosNotas.append([nome, [nota1,nota2], media, situacao])
    decisao = input("Deseja continuar [s/n]? ").strip().upper()
    if decisao not in "N":
        continue
    else:
        break
print("-"*40)
print(f'{"Nº":<5}{"Nome":<15}{"Media":<10}{"Situacao":>10}')
print("-"*40)

for i, a in enumerate(alunosNotas):
    print(f'{i:<5}{a[0]:<15}{a[2]:<10.1f}{a[3]:>10}')
while True:
    show = int(input("Digite aqui o numero do aluno que deseja visualizar as notas (Aperte 999 para sair) "))
    if show == 999:
        break
    else:
        print(f"As nota do aluno {alunosNotas[show -1][0]} foram {alunosNotas[show-1][1]}. Situacao {alunosNotas[show-1][3]}")
print("Volte Sempre")
