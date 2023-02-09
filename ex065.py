exit = ""
sum = 0
count = 0
while exit != "S":
    nu = int(input("digite um numero"))
    if count == 0:
        min = nu
        big = nu
        sum += nu
    elif nu > big:
        big = nu
    elif nu < min:
        min = nu
    count +=1
    exit = input("quer sair?:").upper().strip()[0]
print("A soma dos {} numeros foi de {}, o maior numero foi {} e o menor foi {} e a media entre eles foi de {}".format(count,sum,big,min,sum/count))