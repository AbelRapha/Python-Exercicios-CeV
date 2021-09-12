print("-="*15)
print("      MERCADAO      ")
print("-="*15)
decisao =" "
dict_produtos = {}
while(decisao not in "N"):
    produto = input("Digite o nome do produto: ").strip()
    preco = float(input("Digite o preco do produto "))
    dict_produtos[produto] = preco
    decisao = input("Deseja continuar? ").strip().upper()
    continue
        

print(f"""O valor total da compra foi de R$ {sum(dict_produtos.values())}.\n 
E tiveram {len([produto for produto in dict_produtos if dict_produtos[produto]>1000])} produtos(s) acima de R$ 1.000,00. \n 
Sendo que o produto mais barato foi {min(dict_produtos, key = dict_produtos.get)} e custou R$ {min(dict_produtos.values())}.""")
