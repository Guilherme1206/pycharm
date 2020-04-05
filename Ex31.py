"""Desenvolva um programa que pergunte a distância de uma viagem em Km.
Calcule o preço da passagem, cobrando R$ 0,50 por Km para viagens de até
200Km e R$ 0,45 para viagens mais longas."""

distancia=float(input("Digite a distancia que você vai viajar (em Km):\n"))
if distancia <= 200:
    km = 0.50*distancia
    print(f"O preço para viajar {distancia} km é R${km:.2f}")

else:
    km = 0.45 * distancia
    print(f"O preço para viajar {distancia} km é R${km:.2f}")

input()