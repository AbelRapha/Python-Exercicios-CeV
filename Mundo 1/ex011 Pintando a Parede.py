largura = float(input("Digite a Largura da parede "))
altura = float(input("Digite a altura da parede "))

def area(l,h):
    return l*h
pintura = area(largura, altura)/2

print(f"A area da sua parede representa {area(largura,altura):.2f} m² \nSendo assim, e preciso de {pintura:.2f} litros de tinta")
