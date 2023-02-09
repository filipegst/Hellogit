nome = input("\033[3;31mESCREVA SEU NOME COMPLETO:").strip().upper()
primeira = (nome[0])
print("a primeira letra é {}".format(primeira))
print("ela aparece {} vezes".format(nome.count(primeira)))
print("ela aparece por ultimo na posição {}".format(nome.rfind(primeira)))



