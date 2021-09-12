palavra = input("Digite uma palavra ").strip().lower()

count = palavra.count("a")
first_position = palavra.find("a")+1
last_position = palavra.rfind("a")+1

print("A letra a aparece {} vezes\n E aparece inicialmente na posicao {}\n e a ultima posicao da letra a foi a posicao {}".format(count, first_position, last_position))