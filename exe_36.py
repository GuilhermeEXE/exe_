casa = float(input("Digite o valor da casa: R$ "))
salario = float(input("Digite o seu salário: R$ " ))
anos = int(input("Em quantos anos você irá pagar ? "))

parcelas = casa / anos
minimo = salario * 0.30

if parcelas <= minimo:
    print("Emprestimo concedido.")
    print("O valor total da casa é de {:.2f} R$".format(casa))
    print("O valor total das parcelas é de {:.2f} R$".format(parcelas))
elif parcelas > minimo:
    print("Emprésatimo negado, pois passou dos 30% do limite de seu salário")
