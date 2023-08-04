n1 = float(input("Digite sua nota 1: "))
n2 = float(input("Digite sua nota 2: "))

media = (n1 + n2) / 2

if media < 5:
    print("REPROVADO")
elif media >= 5 and media < 7:
    print("RECUPERAÇÃO")
else:
    print("APROVADO")
print("Sua média final é {:.2f}".format(media))