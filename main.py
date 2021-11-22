import forca

def iniciar_jogo():
    print("*********************************")
    print("*******JGOO DA FORCA!*******")
    print("*********************************")

    jogar = int(input("Digite (1) para iniciar"))

    if (jogar == 1):
        print("Jogando forca")
        forca.jogar_forca()
    else:
        print('Digite (1) para iniciar o jogo! Outras teclas não serão aceitas')

if (__name__ == '__main__'):
    iniciar_jogo()