sexo = str(input("Digite o seu genero [M] ou [F] ")).strip().upper()[0]

while(sexo not in "MmFf"):
    sexo = input("Dados invalidos. Digite o seu genero [M] ou [F] ").strip().upper()

print("Sexo Cadastrado com sucesso! Obrigado!")
