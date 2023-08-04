from time import sleep
max = 5
print("Calculadora Inteligente")
n1 = int(input("Digite o primeiro numero: "))
n2 = int(input("Digite o segundo numero: "))
while max <= 5:
    print("""O que deseja fazer ?
    [1] - SOMAR
    [2] - MULTIPLICAR
    [3] - MAIOR
    [4] - NOVOS NUMERO
    [5] - SAIR""")
    escolha = int(input("Digite sua escolha: "))
    if escolha == 1:
        soma = n1 + n2
        print("A soma entre {} e {} é: {}".format(n1, n2, soma))
    elif escolha == 2:
        multi = n1 * n2
        print("A multiplicação entre {} e {} é: {}".format(n1, n2, multi))
    elif escolha == 3:
        if n1 > n2:
            print("O número {} é maior que {}".format(n1, n2))
        elif n2 > n1:
            print("O número {} é maior que {}".format(n2, n1))
        else:
            print("Números iguais.")
    elif escolha == 4:
        print("Digite os novos numeros abaixo: ")
        n1 = int(input("primeiro numero: "))
        n2 = int(input("segundo numero: "))
    elif escolha == 5:
        print("Saindo...")
        sleep(2)
        break
    else:
        print("Opção inválida. Tente novamente.")
print("Obrigado por usar nosso programa.")