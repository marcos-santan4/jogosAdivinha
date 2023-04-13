import forca
import adivinhacao

def escolher_jogo():
    print("*********************************")
    print("********Escolha seu jogo!********")
    print("*********************************")

    print("(1) Forca \n(2) Adivinhação")
    jogo = int(input("Qual jogo? "))

    if (jogo == 1):
        print("Jogo da Forca")
        forca.jogar()
    elif (jogo == 2):
        print("Jogo da Adivinhação")
        adivinhacao.jogar()

if(__name__ == "__main__"):
    escolher_jogo()