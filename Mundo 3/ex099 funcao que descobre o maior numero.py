def maiorNumero(* num):
    cont = maior = 0
    print("-="*30)
    print("Analisando os valores passados ...")
    for i,v in enumerate(num):
        print(v,end = " ", flush= True)
        cont +=1
        if i ==0:
            maior = v
        else:
            if v > maior:
                maior = v
    print("Foram informados {} valores ao todo".format(cont))
    print("O maior valor informado foi {}".format(maior))
    print("-="*30)
print(maiorNumero(1,2,4,6,3,4,67))
print(maiorNumero(3,8))
print(maiorNumero(1,2))
print(maiorNumero(6))
print(maiorNumero(0))   