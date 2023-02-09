print("==Somador==\nDigite 999 para sair")
count = 0
sum = 0
num = 0
while True:
    num = int(input("Digite um numero :"))
    if num == 999:
        break
    count +=1
    sum += num
print(f"a soma dos {count} numeros é de {sum}")