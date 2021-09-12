num = int(input("Digite um numero: "))
    
for i in range(0,num):
    if i > 1:
        print(f"{(i-2)+(i-1)} ➡  ", end =  "" )            
    else:
        print(f"{i}  ➡  ", end = "")
print(" FIM")    