medida = int(input("Digite um valor em metros "))

def dm(medida):
    return medida*10

def cm(medida):
    return medida*100

def mm(medida):
    return medida*1000

def dam(medida):
    return medida/10

def hm(medida):
    return medida/100

def km(medida):
    return medida/1000

print(f"Convertendo o valor de {medida} m teremos: \n dm: {dm(medida)} dm \n cm: {cm(medida)} cm \n mm: {mm(medida)} mm \n dam: {dam(medida)} dm \n hm: {hm(medida)} hm \n km: {km(medida)} km")
