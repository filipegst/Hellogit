escolha = 5
numeros = "Zero", "Um", "Dois","Tres", "Quatro"
while True:
    escolha = int(input("digite um numero de 0 a 4:"))
    if escolha in [0,1,2,3,4]:
        break
print(numeros[escolha])