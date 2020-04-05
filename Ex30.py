"""Crie um programa que leia um número inteiro e mostre na tela se
ele é par ou impar."""

n=int(input("Digite um número inteiro:\n"))
if n%2 == 0:
    print(f"O numero {n} é par")

else:
    print(f"O número {n} é impar")
input()