"""Escreva um programa que pergunte o salário de um funcionário e calcule
o valor do seu aumento Para salários superiores a R$1.250,00, calcule
um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%."""

salario = float(input("Digite o salário do funcionario:\n"))
if salario <= 1250:
    novosalario = salario * 1.15
else:
    novosalario = salario * 1.1

aumento = novosalario-salario
print(f"O aumento será de R$ {aumento:.2f} e o Salário atualizado \
será de R$ {novosalario:.2f}")

input()