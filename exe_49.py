t = int(input("Digite um número para gerar a tabuada: "))
for c in range(0, 11):
    print("{} x {} = {}".format(t, c, (c*t)))