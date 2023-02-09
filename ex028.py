import math
import random
num = random.randint(1,5)
print(num)
esc = math.trunc(float(input("Adivinha o numero que eu pensei:")))
if esc == num:
    print("Parabens voce adivinhou coretamente")
else:
    print("Voce Errou!!")