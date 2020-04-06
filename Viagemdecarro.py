# -*- coding: utf-8 -*-
"""6) Calcule o tempo de uma viagem de carro. Pergunte a distância a percorrer e a velocidade média"""
distancia = float(input("Digite quantos km você irá percorrer:\n"))
velocidade = float(input("digite a velocidade média em que você irá:(km/h)\n"))
tempo = distancia / velocidade
if tempo < 1:
    print("o tempo que vai levar é", tempo * 60, "minutos")

elif tempo < 0.01:
    print("o tempo que vai levar é", tempo * 60, "segundos")
else:
    print("o tempo que vai levar é", tempo, "horas")
