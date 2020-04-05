"""Escreva um programa para aprovar o empréstimo bancário para a compra
de uma casa. O pragrama vai perguntar o valor da casa, o salário do comprador
e em quatos anos ele vai pagar.
Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30%
do salário ou então o empréstimo será negado."""

casa=float(input("Digite o valor da casa:\n"))
salario=float(input("Digite o  salario do comprador:\n"))
anos=int(input("Digite em quantos anos ele vai pagar:\n"))
prestacao = casa/(anos*12)
if prestacao > salario * 1.3:
    print (f"Infelizmente seu empréstimo foi negado pois\n\
seu salario de R$ {salario} não é suficiente \n\
para pagar uma prestação de R$ {prestacao:.2f}")
else:
    print(f"Seu empréstimo foi aceito, e a sua\n\
prestacao mensal sera de R${prestacao:.2f}")
input()