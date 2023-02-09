minnor = 0
legal = 0
for c in range(1,8):
    age = int(input("digite a idade da {}° pessoa".format(c)))
    if age >= 18:
        legal += 1
    else:
        minnor += 1
print('temos {} pessoas maiores de idade e {} menores de idade'.format(legal,minnor))