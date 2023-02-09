print("==Somador==\nDigite 999 para sair")
count = 0
sum = 0
num = 0
while num != 999:
    num = int(input("Digite um numero :"))
    count +=1
    sum += num
print("a soma dos {} numeros é de {}".format(count-1,sum-999))