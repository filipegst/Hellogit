print("CALCULADORA BASICA")

choice = 0
while choice != 5:
    print("[1]SOMAR"
          "\n[2]SUBTRAIR"
          "\n[3]MULTIPLICAR"
          "\n[4]DIVIDIR"
          "\n[5]SAIR")
    n1 = float(input("Numero 1:"))
    n2 = float(input("Numero 2:"))
    choice = int(input("É escolha uma opção:"))

    if choice == 1:
        print(n1+n2)
    if choice == 2:
        print(n1-n2)
    if choice == 3:
        print(n1*n2)
    if choice == 4:
        print(n1/n2)
    if choice == 5:
        print("Saindo...")
    else:
        print('Opção invalida!!\n')