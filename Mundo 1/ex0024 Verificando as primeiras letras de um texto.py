cidade = input("Digite o nome da sua cidade ").strip()

cidade = cidade.split()
cidade[0] = cidade[0].lower()
confirmacao = cidade[0] == "santo"

print(f"A sua cidade comeca com Santo: {confirmacao}")

#Outro jeito

#print(cidade[:5].upper == "SANTO")