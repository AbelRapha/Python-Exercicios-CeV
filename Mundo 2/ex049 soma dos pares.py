par = [count if count%2==0 else 0 for count in range(2,501,2)]

par = list(filter(lambda a: a != 0, par))

soma = sum(par)
print(soma)
print(len(par))