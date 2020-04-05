import playsound
nome = input("Digite um jogo:")
if nome == "pokemon":
    playsound.playsound("battle.mp3")
elif nome == "zelda":
    playsound.playsound("zelda.mp3")
elif nome == "harvest moon":
    playsound.playsound("harvest.mp3")
else:
    playsound.playsound("fail.mp3")
input()