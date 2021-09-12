c = ('\033[m', #0-sem cores
    '\033[0;30;41m', #1 - Vermelho
    '\033[0;30;43m' # 2 - Amarelo
    );

def titulo(msg,cor = 0):
    tamanho = len(msg)+4
    print(c[cor], end = '')
    print("-"*tamanho)
    print(msg.center(tamanho))
    print("-"*tamanho)
    print(c[0],end='')

def bibliotecas(libs):
    while True:
        if libs in "fim":
            break
        else:
            print(help(libs))
        titulo("Sistema de Ajuda PyHelp",2)
        libs = input("Digite a proxima funcao que deseja consultar ").strip().lower()
    titulo("Obrigado e volte sempre",1)
bibliotecas(libs="print")

        
        