
for c in range(1,5):
    wheigth = float(input("digite o peso da {}° pessoa".format(c)))
    if c == 1:
        biggest = wheigth
        less = wheigth
    if wheigth > biggest:
         biggest = wheigth
    elif wheigth < less:
        less = wheigth
print('o maior peso foi:{} e o menor peso foi:{}'.format(biggest,less))