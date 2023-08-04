print("{:-^40}".format(" LOJAS PARUCCI'S "))
valor = float(input("Digite o valor do produto: R$ "))
print("OPCOES DE PAGAMENTO\n 1 - A VISTA\n 2 - 1X CARTAO\n 3 - 2X NO CARTAO\n 4 - 3X ou MAIS CARTAO")
pag = int(input("Digite a forma de pagamento: "))

if pag == 1:
    print("PAGAMENTO A VISTA, 10% DE DESCONTO")
    total = valor - (valor * 0.1)
    print("O valor total do produto é R$ {:.2f} e com desconto fica R$ {:.2f}".format(valor, total))
elif pag == 2:
    print("CARTAO 1X, 5% DE DESCONTO")
    total = valor - (valor * 0.05)
    print("O valor total do produto é R$ {:.2f} e com desconto fica R$ {:.2f}".format(valor, total))
elif pag == 3:
    print("CARTAO 2X, SEM DESCONTO.")
    parcela = valor / 2
    print("O valor total do produto é R$ {:.2f}".format(valor))
    print("O valor total das parcelas: 2x de R$ {:.2f}".format(parcela))
elif pag == 4:
    print("CARTAO 3X ou MAIS, 20% DE JUROS")
    parcela = int(input("Quantas pacelas ? "))
    total = valor + (valor * 0.2)
    parc = total / parcela
    print("O valor total do produto é R$ {:.2f}".format(valor))
    print("O valor total a pagar é R$ {:.2f}".format(total))
    print("O valor das parcelas: {}x de R$ {:.2f}".format(parcela, parc))
else:
    print("Opcao invalida tente novamente.")
