# -*- coding: UTF-8 -*-

"""Escreva um programa que resolva uma equação de segundo grau."""

#equacao2grau = (a*(x**2))+(b*x)+c

a = float(input("Digite o valor de a:\n"))
b = float(input("Digite o valor de b:\n"))
c = float(input("Digite o valor de c:\n"))

delta = b**2-4*a*c
print ("delta =", delta)

raizdelta=delta**0.5
print ("raiz de delta =", raizdelta)

x1 = (-b+raizdelta)/(2*a)
print("x1 =",x1)
x2 = (-b-raizdelta)/(2*a)
print("x2=",x2)

input()


