# -*- coding: utf-8 -*-

gasolina = input ("Digite o Valor da gasolina:\n")
alcool = input ("Digite o Valor do Alcool:\n")

gasolina_float = float(gasolina) # converte string/texto para inteiro
alcool_float = float(alcool) # converte string/texto para inteiro

valor_real = alcool_float/gasolina_float
valor_justo = 0.70

if valor_real <= valor_justo:
    print ("Ta compensando mais comprar Alcool")

elif valor_real >= valor_justo:
    print ("Ta compensando mais comprar Gasolina")

input ()
