# -*- coding: utf-8 -*-
"""Faça um programa que leia a altura e largura de uma parede em metros, calcule a sua área
e a quantidade de tinta necessaria para pintá-la, sabendo que cada litro de tinta, pinta
uma área de 2m²"""

altura = float(input("Qual a altura da sua parede?\n"))
largura = float(input("Qual a largura da sua parede?\n"))
area = altura*largura
tinta = 2
print(f"Sua área é de {area} m², e você vai precisar de {area/tinta} litros de tinta para pintar sua parede")

