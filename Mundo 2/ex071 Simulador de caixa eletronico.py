print("="*15)
print("    Banco     ")
print("="*15)
valor= int(input("Que valor voce quer sacar? "))
totcedula = 0
cedula = 50
while True:
    if valor >= cedula:
        totcedula += 1
        valor -= cedula
    else:
        if totcedula >0:
            print(f"Ao todo foram {totcedula} cedulas de {cedula}")
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula ==10:
            cedula = 1
        totcedula = 0
        if valor == 0:
            break


