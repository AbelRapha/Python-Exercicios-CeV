impar = [count if count%3 ==0 else 0 for count in range(1,501,2)]

impar = list(filter(lambda a: a != 0, impar))

soma = sum(impar)
print(soma)
print(len(impar))