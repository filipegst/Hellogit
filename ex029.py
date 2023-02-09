velocidade = float(input("Em qual velocidade o carro esta ? : "))
kme =float (velocidade - 80)
multa = float(kme * 7)
if velocidade < 80.01:
    print("obrigado por respeitar o limite de velocidade...dirija com segurança")
else:
    print("voce ultrapassou {}KM do limite de velocidade e sera multado em R${}".format(kme,multa))

