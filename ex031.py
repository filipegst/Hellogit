d = float(input("qual é a distancia da sua viagem?:"))
pro = float((d - 200) * 0.35)
if d < 200:
    print("A sua passagem custara R$:{:.2f}".format(d*0.5))
else:
    print("A sua passagem custara R${:.2f}".format((d*0.5)+ pro))
print(" \n"*6)
print(d,d*0.5,pro)