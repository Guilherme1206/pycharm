"""Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
A multa vai custa R$ 7,00 por cada Km acima do limite."""

km=int(input("Digite a Velocidade atual do carro em Km/h:\n"))
if km > 80:
    multa=(km-80)*7
    print (f"Você está com excesso de velocidade, foi multado em\
 R$ {multa:.2f} reais")
else:
    print("Velocidade dentro do limite, parabéns!")
input()