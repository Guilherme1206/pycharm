import random
chance = random.randrange(8192)
i = 0
while i <= 300000:
    if chance != 0:
        chance = random.randrange(8192)
        i = i+1
    else:
        print(f"A quantidade de encontros até o shiny é: {i}")
        break
