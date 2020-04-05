"""Escreva um programa que leia um número inteiro qualquer
e peça para o usuário escolher qual será a base de conversão:

-1 para binário
-2 para octal
-3 para hexadecimal"""

inteiro = int(input("Digite um número inteiro:\n"))
n = int(input("Digite um número de 1 a 3:\n"))
while n >= 4:
    n = int(input("Você não digitou um número de 1 a 3, tente novamente:\n"))
if n == 1:
    bina = bin(inteiro)
    print(f"{inteiro} em binário é: {bina[2:]}")
elif n == 2:
    octa = oct(inteiro)
    print(f"{inteiro} em octal é: {octa[2:]}")
elif n == 3:
    hexa = hex(inteiro)
    print(f"{inteiro} em hexadecimal é: {hexa.upper()[2:]}")

input()
