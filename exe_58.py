#from random import randint
#computador = randint(0,10) #computador sorteia um numero
#jogador = int(input("Tente acertar o numero: [0 até 10] "))
#soma = 0
#while computador != jogador: # faz o laço de repetição enquanto o jogador erra
#    print("Você errou. Tente novamente!")
#    jogador = int(input("Tente acertar o numero: [0 até 10] "))
#    soma += 1
#    if computador == jogador: # se acertar quebra o laço
#       print("Você acertou")
#print("Você usou {} tentativas.".format(soma))

from random import randint
computador = randint(0, 10)
print("Sou seu computador, acabei de pensar em um numero entre 0 e 10")
print("Tente advinhar...")
acertou = False
palpites = 0
while not acertou:
    jogador = int(input("Digite seu palpite: "))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print("Mais...")
        elif jogador > computador:
            print("Menos...")

print("Acertou com {} tentativas. ".format(palpites))
