s = 0
contador = 0
for c in range(1, 500, 2):
    if (c % 3 == 0):
        s += c
        contador += 1
print("A somas dos {} números é {}".format(contador, s))
