from math import factorial

def fatorial(n,show):
    """
    fatorial(n,show = False)\n
    -> Calcula o Fatorial de um numero.
    :param n: O numero a ser calculado o fatorial
    :param show: (opcional) mostrar ou nao a conta
    :return O valor do fatorial de um numero n
    """
    if show == True:
        for i in range(n,0,-1):
            print(f"{i}", end=" ")
            if i ==1:
                print("",end = '')
            else:    
                print("X",end = ' ')
            
        print("=", factorial(n))
    else:
        print(factorial(n))


print(fatorial(5,show=False))
print(fatorial.__doc__)
