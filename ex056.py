minnor = 0
older = 0
oldname = ""
plusage =int(0)
for c in range(1,5):
    name = (input("==/{}° pessoa\==\nNOME:".format(c)))
    age = int(input("IDADE:"))
    sex = (input("SEXO [M/F]:").upper())
    plusage += age
    if sex == "F" and age <= 18:
        minnor += 1
    if sex == "M" and age > older:
        older = age
        oldname = name
print("{} é o homem mais velho com {} anos ".format(oldname,older))
print("ao todo temos {} mulheres menores de idade".format(minnor))
print("idade media do grupo é de {:.2f}".format(plusage/c))
