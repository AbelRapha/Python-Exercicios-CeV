from datetime import date

lista_genero =[]
lista_nomes = []
lista_idades = []
anoAtual = date.today().year
maior =0
for count in range(1,4):
    print("-"*5, f"{count}ª Pessoa", "-"*5 )
    nome= input("Digite seu Nome: ").strip()
    nascto = int(input("Digite seu ano de nascimento: "))
    genero = input("Digite [F] ou [M] ").strip().upper()
    lista_genero.append(genero)
    lista_nomes.append(nome)
    lista_idades.append(anoAtual - nascto)
    
    if genero == "M":
        if maior < anoAtual - nascto:
            maior = anoAtual-nascto
            homemMaisvelho = nome
    else:
        tot = 0
        if anoAtual - nascto < 20:
            tot += 1
            

print("A media das idades foi de {}".format(sum(lista_idades)/4))
print("O homem mais velho foi {} com {} anos".format(homemMaisvelho, maior))
print("Ha ao todo ha {} mulhere(s) com menos de 20 anos".format(tot))