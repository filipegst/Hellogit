nome = input("qual o seu nome :").strip()
print("seu nome em maiusculas é: {}".format(nome.upper()))
print("seu nome em minusculas é: {}".format(nome.lower()))
print("seu nome possui:{} letras".format(len(nome) - nome.count(" ")))
dividido = (nome.split())
print("seu primeiro nome é {} e possui {} letras".format(dividido[0],len(dividido[0])))
