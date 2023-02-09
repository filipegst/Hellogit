exit = ""
while exit != "S":
    print("termos de uma PA".upper())
    primeiro = int(input("primeiro termo"))
    razao =int(input("razao"))
    decimo = int(input("quantos termos?:"))
    while decimo != 0:
        print(primeiro)
        primeiro = primeiro+razao
        decimo -= 1
    exit = input("quer sair?:").upper()