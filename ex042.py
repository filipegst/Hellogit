r1 = float(input('Digite a primeira reta: '))
r2 = float(input('Digite a segunda reta: '))
r3 = float(input('Digite a terceira reta: '))
if r1+r2 > 3r and r1+r3 > r2 and r2+r3 > r1:
    print('Podem formar um triângulo.')
    if r1== r2 and r2 == r3:
        print("este triangulo é equilatero")
    elif r1 == r2 or r1== r3 or r2 == r3:
        print("este triangulo é isoceles")
    else:
        print("este triangulo é escaleno")
else:
    print('Não podem formar um triângulo.')