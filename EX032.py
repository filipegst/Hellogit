from datetime import date
ano = int(input("que ano quer analizar?, digite 0 para analizar o ano atual :"))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print("O ano de {} é bisexto".format(ano))
else:
    print("O ano de {} não é bisexto".format(ano))