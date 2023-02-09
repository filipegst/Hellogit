import datetime
ano = datetime.date.today().year
nascimento = int(input("em que ano voce nasceu :"))
idade = ano - nascimento
print("voce tem:{} anos".format(idade))
if idade >=20:
    print("sua classificação é master")
elif idade < 20 and idade >=14:
    print("sua classificação é senior")
elif idade <14 and idade >=9:
    print("sua classificação é junior")
else:
    print("sua classificação é mirim")