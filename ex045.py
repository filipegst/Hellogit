import time
import random
print("==JOKENPO!!==")
print('''Opçoes:
[1] Pedra
[2] Papel
[3] Tesoura''')
opcao = int(input('Escolha uma opção:'))
computador = random.randint(1,3)
print("JO")
time.sleep(0.7)
print("KEN")
time.sleep(0.7)
print("POO!!")

if opcao == 1:

    print('Voce: Pedra')
    if computador == 2:
        print("Computador: Papel")
        print("o computador venceu")

    if computador == 3:
        print("Computador: Tesoura")
        print("Parabens Voce venceu!")
    if computador == 1:
        print("Computador:pedra")
        print("Deu empate")

elif opcao == 2:

    print('Voce:Papel')
    if computador == 2:
        print("Computador: Papel")
        print("Deu empate")
    if computador == 3:
        print("Computador: Tesoura")
        print("O computador venceu")
    if computador == 1:
        print("Computador:pedra")
        print("Parabens Voce venceu!")

elif opcao == 3:
    print('Voce:Tesoura')
    if computador == 2:
        print("Computador: Papel")
        print("Parabens Voce venceu!")
    if computador == 3:
        print("Computador: Tesoura")
        print("Deu empate")
    if computador == 1:
        print("Computador:pedra")
        print("O computador venceu")
else:
    print("Computador: PERA! essa opção  não vale")