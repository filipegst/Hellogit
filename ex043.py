peso = float(input("digite o seu peso:"))
altura = float(input("digite sua altura"))
imc = peso/(altura**2)
print("seu IMC é:{:.2f}".format(imc))
if imc >= 40:
    print("voce esta em obesidade morbida")
elif imc <40 and imc >=30:
    print("voce esta obeso")
elif imc <30 and imc >=25:
    print("voce esta em sobrepeso")
elif imc <25 and imc >=18.5:
    print("voce esta no peso ideal")
else:
    print("voce esta abaixo do peso ")