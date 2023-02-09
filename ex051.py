print("os dez primeiros termos de uma PA".upper())
primeiro = int(input("primeiro termo"))
razao =int(input("razao"))
decimo = primeiro + 10 * razao
for c in range (primeiro,decimo,razao):
    print(c)
