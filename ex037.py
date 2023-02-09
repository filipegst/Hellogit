import math
n = int(input('escreva o numero a ser convertido:'))
escolha =int(input("se voce deseja converter o numero em \n binario digite 1\n octal digite 2 \n hexadecimal digite 3: " ))
if escolha == 1:
    print("o numero em binario fica: {}".format(bin(n)))
elif escolha == 2:
    print("o numero em octal fica: {}".format(oct(n)))
elif escolha == 3:
    print("o numero em haxadecimal fica : {}".format(hex(n)))
else:
    print("esta não é uma opção valida")