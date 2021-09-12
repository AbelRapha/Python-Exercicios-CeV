from math import sin, tan, cos, radians

angulo = (float(input("Digite um valor de angulo ")))
angulo_radianos = radians(angulo)
print(f"O valor de sen de {angulo} e {sin(angulo_radianos):.2f} \n O valor de cos {cos(angulo_radianos):.2f} \n O valor da tangente {tan(angulo_radianos):.2f}")