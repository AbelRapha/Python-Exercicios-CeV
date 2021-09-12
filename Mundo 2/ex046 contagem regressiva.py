from time import sleep
for contagem in range(10,-1,-1):
    print(contagem)
    sleep(0.5)
    if contagem == 0:
        print("BUM!! BUM!!")
