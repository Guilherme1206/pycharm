"""Faça um programa que calcule a soma entre todos
os números ímpares que são multiplos de três e que
se encontram no intervalo de 1 até 500"""

s=0
for c in range(1, 501, 1):
    if c%3==0 and c%2==1:
        s += c
        if c>=495:
            print(f"A somatoria é {s}")
input()
