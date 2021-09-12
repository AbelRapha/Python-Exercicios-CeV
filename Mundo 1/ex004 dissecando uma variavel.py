algo = input("Digite algo: ")

print(f" O tipo primitivo do que voce digitou e {type(algo)}")
print(f" So tem espcos? {algo.isspace()}")
print(f"E um numerp? {algo.isnumeric()}")
print(f"E alfabetico? {algo.isalpha()}")
print(f"E alfanumerico {algo.isalnum()}")
print(f"Esta em maiusculas? {algo.isupper()}")
print(f"Esta em maiuscula? {algo.islower()}")
print(f"Esta Capitalizada? {algo.istitle()}")

