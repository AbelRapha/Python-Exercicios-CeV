n = 0
count = 0
totNum = 0
while(n != 999):
    n = int(input("Digite um numero [ou digite 999 para parar] "))
    if n != 999:
        count += n
        totNum += 1
    else:
        break
print("A soma dos {} valores digitados anteriormente foi {}". format(totNum,count))
