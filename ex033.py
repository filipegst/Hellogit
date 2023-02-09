v1 = int(input("digite o primeiro valor:"))
v2 = int(input("digite o segundo valor:"))
v3 = int(input("digite o terceiro valor:"))
maior = v1
menor = v3
if v2 > maior:
    maior = v2
if v3 > maior:
    maior = v3
if v2 < menor:
    menor = v2
if v1 < menor:
    menor = v1
print("o maior numero foi {}".format(maior))
print("o menor numero foi {}".format(menor))
