# -*- coding: UTF-8 -*-

"""Faça um programa que receba duas notas digitadas pelo usuário.
Se a nota for maior ou igual a seis, escreva aprovado, senão escreva reprovado. """

nota1 = float(input("Quanto você tirou na primeira prova?\n"))
nota2 = float(input("Quanto você tirou na segunda prova?\n"))
media = (nota1+nota2)/2

if media >= 6.0:
	print ("Aprovado!!!")
else:
	print ("Reprovado!!!")

input ()