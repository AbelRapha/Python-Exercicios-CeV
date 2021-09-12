name = str(input("Digite seu nome completo ")).strip()

nomeMaiusculo = name.upper()
nomeMinusculo = name.lower()
letras = name.replace(" ", "")

first_name = name.split()

print(f"Seu nome com letras maiusculas: {nomeMaiusculo}\n Em minusculas {nomeMinusculo}\n O nome tem ao todo {len(letras)} letras\n O primeiro nome tem {len(first_name[0])} letras")