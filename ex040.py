n=float(input("digite a primeira nota:"))
n1=float(input('digite a segunda nota:'))
media = (n+n1)/2
print ("a media do aluno foi de {}".format(media))
if media >= 7:
    print("parabens voce foi aprovado!")
elif media <7 and media >= 5:
    print("voce esta em recuperação!")
else:
    print("voce foi reprovado!")
