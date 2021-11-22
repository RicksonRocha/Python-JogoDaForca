import random

def jogar_forca():
    boas_vindas()
    palavra_secreta = sorteia_palavra()

    letras_acertadas = ["_" for letra in palavra_secreta] #list comprehennsions
    print(letras_acertadas)

    enforcou = False
    ganhou = False
    erros = 0

    while(not enforcou and not ganhou):
        chute = solicita_chute()

        if (chute in palavra_secreta):
            letras_acertadas = chute_correto(chute, palavra_secreta, letras_acertadas)
        else:
            erros += 1
            print("Ops, você errou! Faltam {} tentativas.".format(5 - erros))
            desenha_forca(erros)

        enforcou = erros == 5
        ganhou = '_' not in letras_acertadas
        print(letras_acertadas)

    if (ganhou):
        print_ganhou()
    else:
        print_perdeu(palavra_secreta)

def boas_vindas():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

def sorteia_palavra():
    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero_sort = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero_sort].upper()
    return palavra_secreta

def solicita_chute():
    chute = input('Chute uma letra')
    chute = chute.strip().upper()
    return chute

def chute_correto(chute, palavra_secreta, letras_acertadas):
    index = 0
    for letra in palavra_secreta:
        if (chute == letra):
            letras_acertadas[index] = letra
        index += 1
    return letras_acertadas

def print_ganhou():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def print_perdeu(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


if (__name__ == '__main__'):
    jogar_forca()