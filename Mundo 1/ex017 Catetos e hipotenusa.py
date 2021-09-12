from math import hypot

co = float(input("Digite o valor do cateto oposto " ))
ca = float(input("Digite o valor do cateto adjacente "))

print(f"O cumpromento da hipotenusa e {hypot(co,ca):.2f}")