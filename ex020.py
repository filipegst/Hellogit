import random
a1 = input("escreva o nome do primeiro aluno:")
a2 = input("escreva o nome do segundo aluno:")
a3 = input("escreva o nome do terceiro aluno:")
a4 = input("escreva o nome do quarto aluno:")
alunos = [a1,a2,a3,a4]
random.shuffle(alunos)
print(alunos)