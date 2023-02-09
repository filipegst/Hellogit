salario = float(input("digite o salario R$:"))
if salario <= 1400:
    print("o aumento sera de RS:{:.2f}".format((salario*15)//100))
    print("o novo salario sera de R$:{:.2f}".format(salario + ((salario * 15) // 100)))
else:
    print("o aumento sera de RS:{:.2f}".format((salario*10)//100))
    print("o novo salario sera de R$:{:.2f}".format(salario + ((salario * 10) // 100)))