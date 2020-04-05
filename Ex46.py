from time import sleep
"""Faça um programa que mostre na tela uma
contagem regressiva para o estouro de fogos
de artificio, indo de 10 até 0, com uma pausa de
1 segundo entre eles."""
print("CONTAGEM REGRESSIVA PARA O ESTOURO DE FOGOS DE ARTIFICIO")
print("—*— "*14)
for c in range(10,0,-1):
    print(c)
    sleep(1)
print("\033[1;31m******BOOM******\033[m")
input()