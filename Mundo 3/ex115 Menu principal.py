from time import sleep

def linha(tam = 42):
    return '-'*tam

def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())

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

def menu(lista):
    cabecalho("Menu")
    cont = 1
    for item in lista:
        print(f'\033[33m{cont}\033[m - \033[34m{item}\033[m')
        cont +=1
    print(linha())
    opc = leiaInt("\033[33mSua Opcao:\033[m ")
    return opc

def ArquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else: 
        return True

def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
    except:
        print("Houve um ERRO na criacao do arquivo")
    else:
        print(f'Arquivo {nome} criado com sucesso')

def lerArquivo(nome):
    try: 
        a = open(nome, 'rt')
    except:
        print("Erro ao ler o arquivo")
    else:
        cabecalho('Pessoas Cadastradas')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')

def Cadastrar(nomeDoArquivo, nomeDaPessoa = 'Desconhecido', idade = 0):
    try:
        a = open(nomeDoArquivo,'at') #at -> append informacoes no arquivo
    except:
        print('Houve um erro na abertura do arquivo')
    else:
        try:
            a.write(f'{nomeDaPessoa}; {idade}\n')
        except:
            print("Houve um ERRO na hora de escrever os dados")
        else:
            print(f'Novo registro de {nomeDaPessoa} adicionado')
            a.close()


arquivo = 'ex115.txt'

if not ArquivoExiste(arquivo):
    criarArquivo(arquivo)
     
cabecalho("Sistema Arquivo v1.0") 


while True:
    resp = menu(['Listar Pessoas','Cadastrar Pessoas','Sair do Sistema'])
    if resp ==1:
        #Opcao de listar pessoas
        lerArquivo(arquivo)
    elif resp ==2:
        #Opcao de cadastrar pessoas
        nome = input("Nome: ").strip()
        idade = int(input("Idade: "))
        Cadastrar(arquivo, nome, idade)
    elif resp ==3:
        cabecalho("Saindo do Sistema... Ate Logo!")
        break
    else:
        print("\033[31mERRO! Digite uma opcao valida\033[m")
    sleep(1)