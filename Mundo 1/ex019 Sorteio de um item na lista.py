import random as rd

aluno1 = str(input("Digite o nome do primeiro aluno: "))
aluno2 = str(input("Digite o nome do segundo aluno: "))
aluno3 = str(input("Digite o nome do terceiro aluno: "))
aluno4 = str(input("Digite o nome do quarto aluno: "))

lista_alunos = [aluno1,aluno2,aluno3]

print(f"O aluno sorteado que ira limpar o quadro hoje e o {rd.choice(lista_alunos)}")