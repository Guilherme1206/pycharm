"""Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar
que tipo de triângulo será formado:

-Equilátero: todos os lados iguais
-Isósceles: dois lados iguais
-Escaleno: todos os lados diferentes"""

a=float(input("Digite o valor da reta a:\n"))
b=float(input("Digite o valor da reta b:\n"))
c=float(input("Digite o valor da reta c:\n"))
equilatero = a == b == c
isosceles = c != a == b or b!= a == c or a != b == c
escaleno = a != b != c != a
#print(equilatero,isosceles,escaleno)
if (b - c) < a < (b + c) and (a - c) < b < (a + c) and (a - b) < c < (a + b):
    print("Elas podem formar um triangulo")
    if equilatero == True:
        print ("e o triangulo é \033[1;31mequilatero!\033[m")
    elif isosceles == True:
        print("e o triangulo é \033[1;31misosceles!\033[m")
    elif escaleno == True:
        print("e o triangulo é \033[1;31mescaleno!\033[m")
else:
    print("Elas não podem formar um Triangulo!")
input()