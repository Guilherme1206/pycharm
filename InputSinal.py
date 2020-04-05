# -*- coding: UTF-8 -*-

""" Escreva um programa que receba dois números e um sinal,
e faça a operação matemática definida pelo sinal. """

primeironumero = input("Digite o primeiro numero:\n")
#isinstance(primeironumero,float)
while primeironumero.isnumeric() == False:
	primeironumero = input("Valor invalido, Digite o primeiro numero:\n")

segundonumero = input("Digite o segundo numero:\n")

while segundonumero.isnumeric() == False:
	segundonumero = input("Valor invalido, Digite o segundo numero:\n")

sinal = input("Digite o Sinal (+-/*)\n")

while sinal != "+" and sinal != "-" and sinal != "*" and sinal != "/":
	sinal = input("Valor invalido, Digite apenas Sinal (+-/*)\n")

primeironumerofloat = float(primeironumero)
segundonumerofloat = float(segundonumero)

if sinal == "+":
	print ("A resposta é", primeironumerofloat+segundonumerofloat)
elif sinal == "-":
	print ("A resposta é", primeironumerofloat-segundonumerofloat)
elif sinal == "*":
	print ("A resposta é", primeironumerofloat*segundonumerofloat)
elif sinal == "/":
	print ("A resposta é", primeironumerofloat/segundonumerofloat)

input()
