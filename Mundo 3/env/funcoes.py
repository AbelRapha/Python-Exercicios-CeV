def fatorial(n):
    f =1
    for i in range(1,n+1,1):
        f *= i 
    return f

def dobro(n):
    return 2*n

def triplo(n):
    return 3*n

def aumentar(n,p):
    return n + n*p/100

def diminuir(n,p):
    return n - n*p/100

def metade(n):
    return n/2

def resumo(n,a,d):
    print("-"*30)
    print(f"{'Resumo'.center(30)}")
    print("-"*30)
    dicionario = dict()
    n = float(n)
    dicionario['Preco analisado'] = n
    dicionario['Dobro do Preco'] = dobro(n)
    dicionario['Metade de Preco'] = metade(n)
    if a != 0:
        dicionario[f"{a}% de aumento"] = aumentar(n,a)
    if d != 0:
        dicionario[f'{d}% de reducao'] = diminuir(n,d)
    for k,v in dicionario.items():
        print(f'{k:<3}: {v:>10}')
    print("-"*30)
    
def leiadinheiro(palavra):
    while True:
        if palavra.isalpha():
            print("ERRO!! Digite um valor valido.")
            palavra = input("Digite um valor: ").strip().replace(',','.')           
        else:
            break
    return float(palavra)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
