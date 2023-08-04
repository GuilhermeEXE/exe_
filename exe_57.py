sexo = str(input("Digite seu sexo: ")).strip().upper()[0]
while sexo not in "MF":
    sexo = str(input("Digite seu sexo: ")).strip().upper()[0]
print("Sexo {} informado com sucesso.".format(sexo))
