"""Crie um programa que mostre na tela todos os números
pares que estão no intervalo entre 1 e 50."""
print("Os números pares entre 1 e 50 são:")

for c in range(1, 51, 2):
    if c<=48:
        print(c + 1, end=", ")
    else:
        print(c + 1, end="")
input()
