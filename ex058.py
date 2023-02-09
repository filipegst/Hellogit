import math
import random
error = 0
num = random.randint(1,5)
esc = math.trunc(float(input("Adivinha o numero que eu pensei:")))
while esc != num:
    print("Voce Errou!!")
    esc = math.trunc(float(input("Adivinha o numero que eu pensei:")))
    error += 1
if error > 0:
    print("Voce acertou, mas precisou de {} tentativas".format(error+1))
else:
    print("\033[32mVoce acertou de primeira!")