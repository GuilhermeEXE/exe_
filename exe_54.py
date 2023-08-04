from datetime import date
ano = date.today().year
maior = 0
menor = 0
for c in range(1, 8):
    idade = int(input("Digite o ano de nascimento da {}° pessoa: ".format(c)))
    if ano - idade >= 18:
        maior = maior + 1
    else:
        menor = menor + 1
print("Quantidade de maiores de idade: {}".format(maior))
print("Quantidade de menores de idade: {}".format(menor))
