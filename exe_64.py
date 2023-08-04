num = cont = soma = 0
num = int(input("Digite um numero: "))
while num != 999:
    soma += num
    cont += 1
    num = int(input("Digite um numero: "))
print("Você digitou {} numeros e a soma entre eles é {} ".format(cont, soma))
