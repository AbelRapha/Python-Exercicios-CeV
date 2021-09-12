def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print()
            print("\033[033mERRO! Por favor, digite um numero inteiro valido\033[m")
            continue
        except KeyboardInterrupt:
            print()
            print("\033[033mEntrada de dados interrompida pelo usuario\033[m")
            return 0
        else:
            return n
        
def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print()
            print("\033[033mERRO! Por favor, digite um numero real valido\033[m")
            continue
        except KeyboardInterrupt:
            print()
            print("\033[033mEntrada de dados interrompida pelo usuario\033[m")
            return 0
        else:
            return n



n1 = leiaInt('Digite um valor inteiro: ')
n2 = leiaFloat("Digite um valor real: ")
print(f'O valor inteiro digitado foi {n1} e o real foi {n2}')
