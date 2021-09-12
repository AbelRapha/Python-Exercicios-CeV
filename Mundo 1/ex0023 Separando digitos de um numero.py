numero = int(input("Digite um numero inteiro de 0 a 9999 "))

u = numero//1 %10
d = numero//10 %10
c = numero//100%10
m = numero//100%10

print(f"unidade: {u} \n dezena: {d} \n centena: {c}\n milhar: {m}")
