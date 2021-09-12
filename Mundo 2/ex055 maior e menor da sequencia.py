lista_pesos = []
for count in range(1,6):
    peso = input("Digite o peso da {}ª pessoa:".format(count)).strip().replace(",",".")
    peso = float(peso)
    lista_pesos.append(peso)
    


print(f"O maior peso foi {max(lista_pesos)} e o menor peso foi {min(lista_pesos)}")