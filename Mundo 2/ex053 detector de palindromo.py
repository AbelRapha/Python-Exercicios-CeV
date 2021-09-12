palavra = input("digite uma palavra ").strip().upper()
palavra_lista = palavra.split()
palavra_junto = "".join(palavra_lista)
#Ou inverso = palavra_junto[::-1]
inverso = ''
for letra in range(len(palavra_junto)-1, -1,-1):
    inverso += palavra_junto[letra]
if palavra_junto == inverso:
    print("A palavra {} e um PALINDROMO".format(palavra))
else:
    print("A palavra {} nao e  PALINDROMO`")