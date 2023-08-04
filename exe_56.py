somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomehomemvelho = ''
totmulher20 = 0
for p in range(1,5):
    print("---- {}° PESSOA ----".format(p))
    nome = str(input("Digite seu nome: ")).strip()
    idade = int(input("Digite sua idade: "))
    sexo = str(input("Digite seu sexo: [M/F] ")).strip()
    somaidade += idade
    if p == 1 and sexo in "Mm":
        maioridadehomem = idade
        nomehomemvelho = nome
    if sexo in "Mm" and idade > maioridadehomem:
        maioridadehomem = idade
        nomehomemvelho = nome
    if sexo in "Ff" and idade < 20:
        totmulher20 += 1
mediaidade = somaidade / 4
print("A média de idades é {:.2f} anos".format(mediaidade))
print("O homem mais velho tem {} anos e se chama {}".format(maioridadehomem, nomehomemvelho))
print("São {} mulher(es) menores de 20 anos".format(totmulher20))
