import random

def jogar():

    print("**********************************")
    print("Bem vindo aos jogo de adivinhação!")
    print("**********************************")

    numero_secreto = random.randrange(1,101)
    total_de_tentativas = 0
    pontos = 1000

    print("Qual o nível de Dificuldade?")
    print(" (1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Define nível:"))
    if nivel == 1:
        total_de_tentativas = 20
    elif nivel == 2:
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for rodada in range (1, total_de_tentativas + 1):
        print("Tentativa {} de {}". format (rodada, total_de_tentativas))
        chute_str = input("Digite seu numero: ")
        print("Você Digitou", chute_str)
        chute = int(chute_str)

        if (chute <1 or chute > 100):
            print ("Digite um número de  1 a 100!")
            continue

        acertou = (chute == numero_secreto)
        maior   = (chute > numero_secreto)
        menor   = (chute < numero_secreto)


        if(acertou):
            print("Você acertou e fez {} pontos!".format(pontos))
            break
        else:
            if (maior):
                print("Você errou! Seu chute foi maior que o Número secreto")
            elif (menor):
                print("Você errou! Seu chute foi menor que o Número secreto")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

    print("Fim de jogo")

if(__name__ == "__main__"):
    jogar()