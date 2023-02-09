v1 = int(input("digite o primeiro valor:"))
v2 = int(input("digite o segundo valor:"))
maior = v1
if v2 > maior:
    maior = v2
    print("o segundo numero: {} foi o maior".format(maior))
elif v1 == v2:
    print("os dois numeros são iguais")
else:
    print("o primeiro numero:{} foi o maior".format(maior))
