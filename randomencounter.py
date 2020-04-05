import random
chance = random.randrange(8192)
teste = random.randrange(8192)
i = 0
while i <= 50000:
    if chance != teste:
        chance = random.randrange(8192)
        teste = random.randrange(8192)
        i = i+1
    else:
        print(f"A quantidade de encontros até o shiny é: {i}")
        break
