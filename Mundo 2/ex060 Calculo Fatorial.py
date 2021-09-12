num = int(input("Digite um numero: "))


n = num
f = 1
print(f"O fatorial de {num} e")
while(n > 0):
    print("{}".format(n), end = '')
    print(" x " if n > 1  else '=', end= '')
    f *= n
    n -=1
print(f)    

#Utilizando for
num = int(input("Digite um numero: "))
n = num
f = 1
for count in range(num,0,-1):
    print("{}".format(n), end = '')
    print(" x " if n > 1 else "=" ,end = '')
    f *= count
    n -= 1
print(f)
