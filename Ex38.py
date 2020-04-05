"""Escreva um programa que leia dois números inteiros e compare-os,
mostrando na tela uma mensagem:

- O primeiro valor é maior
- O segundo valor é maior
-Não existe valor maior, os dois são iguais"""

n1 = int(input("Digite o primeiro número inteiro:\n"))
n2 = int(input("Digite o segundo número inteiro:\n"))

if n1 > n2:
    print(f"O primeiro valor é o maior!")
elif n1 < n2:
        print(f"O segundo valor é o maior!")
elif n1 == n2:
        print(f"Não existe valor maior, os dois são iguais!")

input()
