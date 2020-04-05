"""024: Crie um programa que leia o nome de uma cidade diga
se ela começa ou não com o nome "SANTO"."""

n = input("Digite o nome de uma cidade:").strip().upper()
nsplit = n.split()
if nsplit[0][0:5] == 'SANTO':
    print("Ela começa com santo!!!")
else:
    print ("Ela não começa com santo!!!")
