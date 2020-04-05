import random
"""Crie um programa que faça o computador jogar JoKenPô com você."""

pedra=0
papel=1
tesoura=2
computador=random.randint(0,2)
print("Computador: Tente ganhar de mim no Jokenpo hahaha")
player = int(input("Digite [0] para pedra\n\
Digite [1] para papel\n\
Digite [2] para tesoura\n"))

if player == 0 and computador == 0:
    print("Você colocou Pedra e o computador colocou Pedra")
    print("Deu empate!")
elif player == 0 and computador == 1:
    print("Você colocou Pedra e o computador colocou Papel")
    print("HAHAHA! Você perdeu! papel ganha de pedra")
elif player == 0 and computador == 2:
    print("Você colocou Pedra e o computador colocou tesoura")
    print("Droga! Você venceu, pedra ganha de tesoura!")
elif player == 1 and computador == 0:
    print("Você colocou Papel e o computador colocou Pedra")
    print("Droga! Você venceu, papel ganha de pedra!")
elif player == 1 and computador == 1:
    print("Você colocou Papel e o computador colocou Papel")
    print("Deu empate!")
elif player == 1 and computador == 2:
    print("Você colocou Papel e o computador colocou Tesoura")
    print("HAHAHA! Você perdeu! tesoura ganha de papel")
elif player == 2 and computador == 0:
    print("Você colocou Tesoura e o computador colocou Pedra")
    print("HAHAHA! Você perdeu! pedra ganha de tesoura")
elif player == 2 and computador == 1:
    print("Você colocou Tesoura e o computador colocou Papel")
    print("Droga! Você venceu, tesoura ganha de papel!")
elif player == 2 and computador == 2:
    print("Você colocou Tesoura e o computador colocou Tesoura")
    print("Deu empate!")
input()