print("Lojas Baratara")
price = 0
expensive = 0
lower = 1
cheap = ""
tot = 0
while True:
    product = input("Nome do Produto:").strip()
    price = float(input("Qual é o valor R$:"))
    if tot == 0:
        cheap = product
        lower = price
    tot += price
    if price > 1000:
        expensive += 1
    if price < lower:
        cheap = product
        lower = price
    ext = ""
    while ext != 'S' and ext != 'N':
            ext = input("quer continuar ? [S/N]:").strip().upper()[0]
    if ext == "N":
        print(f"O valor total gasto foi de R$:{tot}, o produto mais barato foi {cheap}, custando {lower}\n"
              f" E voce possui {expensive} produtos que custam mais de mil reais ")
        break

