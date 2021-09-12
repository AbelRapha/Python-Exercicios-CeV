decisao = ''
lista_numeros = []
while(decisao != "N"):
   num = input("Digite um numero ")
   decisao = input("Quer continuar? [S/N] ").strip().upper()
   lista_numeros.append(num)
   if decisao not in "N":
       continue
   else:
       break
#convertendo lista de numeros para todos os elementos do tipo inteiro
for item in range(0, len(lista_numeros)):
    lista_numeros[item] = int(lista_numeros[item])
print(f"Voce digitou {len(lista_numeros)} numeros e a media foi de {sum(lista_numeros)/len(lista_numeros)} \n O maior valor foi {max(lista_numeros):.1f} e o menor valor foi o {min(lista_numeros)}")
