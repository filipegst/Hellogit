totage = 0
totm = 0
totfem = 0
age = 0
while True:
    sex = ""
    print("CADASTRE UMA PESSOA")
    print("_"*20)
    age = int(input("Idade:"))
    while sex !="M" and sex!="F":
        sex = input("Sexo: [M/F]").strip().upper()[0]
    if age >= 18:
        totage += 1
    if sex == "M":
        totm += 1
    elif sex == "F" and age >= 20:
        totfem += 1
    while ext != "S" and ext != "n":
        ext = input("quer continuar: [S/N]").strip().upper()[0]
    if ext == 'N':
         print(f"temos ao todo {totage} pessoas maiores de idade, {totm} deles são homens e {totfem} são mulheres com mais de 20 anos")
         break
