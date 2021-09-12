distancia = int(input("Digite a distancia da viagem em km: "))

def cobranca(dist):
    if dist <= 200:
        return dist*0.5
    else:
        return dist*0.45

        
print(f"O custo da sua viagem sera de R$ {cobranca(distancia)}")
