number = int(input("me diga o numero que voce quer saber se é primo ?:"))
plusc = 0
for c in range (1,number+1):
    if number%c == 0:
        print('\033[32m', c, end=".")
        plusc += 1
    else:
        print('\033[31m', c, end='.')
if plusc == 2:
            print("\n o numero {} é primo".format(number).upper())
else:
    print("\033[31m\n {} não é primo, ele foi divisivel {} vezes".format(number,plusc).upper())


