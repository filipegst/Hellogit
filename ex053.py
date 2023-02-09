phrase = input("DETECTOR DE PALINDROMOS:").strip().upper().replace(" ","")

nun = len(phrase)
invert =""
for c in range(nun-1,-1,-1):
    invert += phrase[c]
if phrase == invert:
    print("ESTA FRASE É UM PALINDROMO")
else:
    print("{} É DIFERENTE DE {}".format(invert,phrase))
