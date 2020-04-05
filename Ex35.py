"""Desenvolva um programa que leia o comprimento de três retas e diga
ao usuário se ela podem ou não formar um triângulo."""

a=float(input("Digite o valor da reta a:\n"))
b=float(input("Digite o valor da reta b:\n"))
c=float(input("Digite o valor da reta c:\n"))

if (b - c) < a < (b + c) and (a - c) < b < (a + c) and (a - b) < c < (a + b):
    print("Elas podem formar um \033[1;31mTriangulo!\033[m")
else:
    print("Elas não podem formar um Triangulo!")
input()