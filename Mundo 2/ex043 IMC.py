peso = float(input("Digite o sue peso em Kg: "))
altura = input("Digite sua altura em metros: ").strip().replace(",",".")
altura = float(altura)

def IMC(peso,altura):
    imc = peso/(altura**2)
    if imc < 18.5:
        return f"seu IMC e de {imc:.1f} ABAIXO DO PESO"
    elif imc >= 18.5 and imc < 25:
        return f"seu IMC e de {imc:.1f} PESO NORMAL"
    elif imc >=25 and imc < 30:
        return f"seu IMC e de {imc:.1f} SOBREPESO"
    elif imc >=30 and imc < 40:
        return f"seu IMC e de {imc:.1f} OBESO"
    else:
        return f"seu IMC e de {imc:.1f} OBESIDADE GRAVE"

print(IMC(peso,altura))