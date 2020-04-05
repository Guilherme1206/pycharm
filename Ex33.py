"""Faça um programa que leia três números e mostre qual é o maior
e qual é o menor."""

n1=float(input("Digite o primeiro número: \n"))
n2=float(input("Digite o segundo número: \n"))
n3=float(input("Digite o terceiro número: \n"))

if n1>n2 and n1>n3:
    print(f"O número {n1} é o maior")
    if n2<n3:
        print(f"e o número {n2} é o menor")
    elif n3<n2:
        print(f"e o número {n3} é o menor")
    else:
        print(f"e outros dois números são igualmente os menores")
elif n2 > n1 and n2 > n3:
    print(f"O número {n2} é o maior")
    if n1<n3:
        print(f"e o número {n1} é o menor")
    elif n3<n1:
        print(f"e o número {n3} é o menor")
    else:
        print(f"e outros dois números são igualmente os menores")
elif n3 > n1 and n3 > n2:
    print(f"O número {n3} é o maior")
    if n2<n1:
        print(f"e o número {n2} é o menor")
    elif n1<n2:
        print(f"e o número {n1} é o menor")
    else:
        print(f"e outros dois números são igualmente os menores")
elif n1== n2 and n2 == n3 or n1==n3:
    print(f"Você digitou números iguais!")

input()