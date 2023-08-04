nascimento = int(input("Digite a data de nascimento: "))

idade = 2023 - nascimento

if idade <= 9:
    print("MIRIM")
elif idade >= 9 and idade <= 14:
    print("INFANTIL")
elif idade >= 14 and idade <= 19:
    print("JUNIOR")
elif idade >= 19 and idade <=20:
    print("SENIOR")
else:
    print("MASTER")