import random

def jogar_adivinhacao():
    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")

    numero_secreto = round(random.randrange(1, 101))
    rodada = 1
    tentativas = 3
    pontos = 1000

    print('Selecione o nível de dificuldade')
    print('(1).Fácil (2).Médio (3).Difícil')
    nivel = int(input('Digite o nível: '))

    if (nivel == 1):
        tentativas = 10
    elif (nivel == 2):
        tentativas = 7
    else:
        tentativas = 3

    while (rodada <= tentativas):
        print('Tentativa', rodada, 'de', tentativas)

        chute = input('Adivinhe o número entre 1 e 100')
        chute_int = int(chute)

        if (chute_int < 1 or chute_int > 100):
            print('Apenas entre 1 e 100')
            continue

        acertou = chute_int == numero_secreto
        maior = chute_int > numero_secreto
        menor = chute_int < numero_secreto

        if (acertou):
            print('Voce acertou e fez {} pontos!'.format(pontos))
            print('Acertou')
            break
        else:
            if (maior):
                print('Chute maior que o número secreto')
            elif (menor):
                print('Chute menor que o número secreto')
            pontos_perdidos = abs(numero_secreto - chute_int)
            pontos = pontos - pontos_perdidos
        rodada = rodada + 1

    print('Fim de jogo')