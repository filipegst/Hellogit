casa = float(input('Qual é o valor da casa: '))
salario = float(input('qual é o seu salario: '))
ano = float(input('em quantos anos voce ira quitar a casa:'))
prestaçao = casa/(ano*12)
if prestaçao <= salario *30 / 100:
      print("voce ira pagar prestaçoes de R$:{:.2f}".format(prestaçao))
else:
      print("voce não pode financiar esta casa!")

