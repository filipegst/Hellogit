while True:
    print('~~~~~~~~~~TABUADA~~~~~~~~')
    nu = int(input('digite o numero a ser consultado:'))
    print('#####Resultado#####')
    if nu < 0:
        break
    aux = 1
    while aux <= 10:
        print(f'   {aux} X {nu} = {aux * nu}')
        aux += 1

print('##### FIM DO PROGRAMA #####')
