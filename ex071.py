print("Caixa Eletronico")
valor = int(input("Qual é o valor que voce vai sacar? R$:"))
ced = 50
total = 0
while True:
    if valor >= ced:
        valor -= ced
        total += 1
    else:
        if total > 0:
            print(f"voce ira receber {total} cedulas de {ced}")
        if ced == 50:
            ced = 20
        elif ced ==20:
            ced = 10
        elif ced == 10:
            ced = 1
        total = 0
        if valor == 0:
            break
