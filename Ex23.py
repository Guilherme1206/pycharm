"""023: Faça um programa que leia um número de 0 a
9999 e mostre na tela cada um dos dígitos separados."""

n = int(input("Digite um número de 0 a 9999:"))

while n >= 10000:
    n = int(input("Digite um número entre 0 e 9999:"))

if n >=1000:
    nstr = str(n)
    milhar = nstr[0]
    centena = nstr[1]
    dezena = nstr[2]
    unidade = nstr[3]
    print(f"Unidade: {unidade}\
    \nDezena: {dezena}\
    \nCentena: {centena}\
    \nMilhar: {milhar}")

elif n>=10 and n<=99:
    nstr = str(n)
    milhar = 0
    centena = 0
    dezena = nstr[0]
    unidade = nstr[1]
    print(f"Unidade: {unidade}\
    \nDezena: {dezena}\
    \nCentena: {centena}\
    \nMilhar: {milhar}")

elif n>=0 and n<=9:
    nstr = str(n)
    milhar = 0
    centena = 0
    dezena = 0
    unidade = nstr[0]
    print(f"Unidade: {unidade}\
    \nDezena: {dezena}\
    \nCentena: {centena}\
    \nMilhar: {milhar}")
else:
    nstr = str(n)
    milhar = 0
    centena = nstr[0]
    dezena = nstr[1]
    unidade = nstr[2]
    print(f"Unidade: {unidade}\
    \nDezena: {dezena}\
    \nCentena: {centena}\
    \nMilhar: {milhar}")