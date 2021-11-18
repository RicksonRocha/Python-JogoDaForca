def jogar_forca():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    palavra_secreta = 'mochileiro'
    enforcou = False
    acertou = False

    while(not enforcou and not acertou):
        chute = input('Chute uma letra')

        index = 0
        for letra in palavra_secreta:
            if (chute == letra):
                print('Letra {} encotrada na posicao {}'.format(letra, index))
            index = index + 1

        print('jogando')

    print("Fim do jogo")

if (__name__ == '__main__'):
    jogar_forca()