primeiro = int(input("Primeiro termo: "))
razao = int(input("Razao da PA: "))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print("{} -> ".format(termo), end = '')
        termo += razao
        cont += 1
    print("PAUSA")
    mais = int(input("Quantos temos você quer mostrar a mais ? "))
print("Finalizada com {} termos".format(total))
