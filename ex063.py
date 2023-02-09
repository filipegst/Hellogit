print("SEQUENCIA DE FIBONACCI")
n1 = 0
n2 = 1
cont = int(input("Quantos termos quer ver da sequencia?: "))
while cont != 0:
    print(n1,n2, end =" " )
    n1 += n2
    n2 = n1 + n2
    cont -= 1