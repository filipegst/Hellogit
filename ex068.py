import random
while True:
    resp = ""
    while resp != "P" and resp!= "I":
        resp = input("Vamos Jogar, Par ou IMPAR:").upper().strip()[0]
    n = int(input('Um do lá si:'))
    print("JÁ!")
    comp = random.randint(0,10)
    print(comp)
    if (n + comp) % 2 == 0:
        print(f'O número {n+comp} é PAR!')
        if resp == ('P'):
            print("voce venceu")
        else:
            print("voce perdeu")
            break
    else:
        print(f'O número é {n+comp} ÍMPAR!')
        if resp == ('R'):
            print("voce venceu")
        else:
            print("voce perdeu")
            break