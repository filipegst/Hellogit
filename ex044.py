print('CALCULADOR DE COMPRAS E JUROS!')
valor = float(input('Qual é o valor da compra R$:'))
print('escolha a forma de pagamento\n [1]DINHEIRO \n [2]DEBITO \n [3]CREDITO A VISTA \n [4]CREDITO PARCELADO ')
pagamento = int(input('  '))
if pagamento == 1:
    print("Pagamento em dinheiro possui 12% de desconto\nO desconto sera de {} a compra ficara em {}".format(valor*12/100,valor - (valor*12/100)))
elif pagamento == 2:
    print('Pagamento em debito possui 10% de desconto\nO desconto sera de {} a compra ficara em {}'.format(valor*10/100,valor - (valor*10/100)))
elif pagamento == 3:
    print('Pagamento em credito a vista  possui 5% de desconto\nO desconto sera de {} a compra ficara em {}'.format(valor*5/100,valor - (valor*5/100)))
elif pagamento == 4:
    parcela =int(input('Em quantas parcelas pretende pagar:'))
    if parcela == 1:
        print('Pagamento em credito a vista  possui 5% de desconto\nO desconto sera de {} a compra ficara em {}'.format(
            valor * 5 / 100, valor - (valor * 5 / 100)))
    else:
        print('Pagamento em credito parcelado possui juros\nO juros sera de {} a compra ficara em {}'.format(valor * parcela / 100, valor + (valor * parcela / 100)))
else:
    print("Esta não é uma opção valida")
