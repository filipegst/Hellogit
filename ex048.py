soma=0
cont=0
for c in range (0,501):
 if (c%3 ==0) and c % 2 != 0:
  cont= cont+1
  soma = soma+c
print (cont)
print(soma)