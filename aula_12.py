nome = str(input("Qual é seu nome ? "))
if nome == 'Gustavo':
    print("Que nome bonito")
elif nome == "Pedro" or nome == "Guilherme":
    print("Nome popular em")
else:
    print("Nome normal em")
print("Tenha um bom dia {}".format(nome))
