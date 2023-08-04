nascimento = int(input("Digite sua data de nascimento: "))

idade = 2023 - nascimento

if idade < 17:
    print("Ainda nao esta na hora")
    conta = 17 - idade
    print("Faltam {} anos".format(conta))
elif idade >= 17 and idade <= 18:
    print("Esta na hora de se alistar")
else:
    print("Já passou o tempo de se alistar.")
    conta = idade - 18
    print("Se passaram {} anos ".format(conta))