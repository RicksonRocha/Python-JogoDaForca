import random

def jogar_forca():
    boas_vindas()
    palavra_secreta = sorteia_palavra()

    letras_acertadas = ["_" for letra in palavra_secreta] #list comprehennsions

    enforcou = False
    acertou = False
    erros = 0

    while(not enforcou and not acertou):
        chute = input('Chute uma letra')
        chute = chute.strip().upper()

        if (chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if (chute == letra):
                    letras_acertadas[index] = letra
                index += 1
        else:
            erros += 1
            print("Ops, você errou! Faltam {} tentativas.".format(6 - erros))

        enforcou = erros == 8
        acertou = '_' not in letras_acertadas
        print(letras_acertadas)

    if (acertou):
        print('Voce acertou!')
    else:
        print('Voce perdeu!')

    print("Fim do jogo")

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

if (__name__ == '__main__'):
    jogar_forca()