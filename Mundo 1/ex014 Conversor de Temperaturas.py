temp = float(input("Digite a temperatura em celsius "))

def farenheit(temp):
    return (temp*9)/5 + 32


print(f"O valor da temperatura convertido para Farenheits e {farenheit(temp):.2f} ")
