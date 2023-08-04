p = int(input("Digite o primeiro termo: "))
r = int(input("Digite a razao: "))
for c in range(1, 11):
    an = p + (c - 1) * r
    print(an, end= " -> ")
print("FIM")