import datetime
ano = datetime.date.today().year
nascimento = int(input("em que ano voce nasceu :"))
idade = ano - nascimento
print("voce tem:{} anos".format(idade))
if idade == 18:
    print("voce ira se alistar este ano")
elif idade > 18:
    print("voce já se alistou faz {} anos".format(idade - 18))
elif idade < 18:
    print("voce vai se alistar em {} anos".format(18 - idade))
