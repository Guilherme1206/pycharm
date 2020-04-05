"""022: Crie um programa que leia o nome completo de uma pessoa
e mostre: - O nome com todas as letras maiúsculas e minúsculas.
- Quantas letras ao TO DO (sem considerar espaços).
- Quantas letras tem o primeiro nome."""

nome = input("Digite seu nome:")
print("Seu nome em maiuscula é:\n", nome.upper())
print("Seu nome em minuscula é:\n", nome.lower())
espaco = len(nome.replace(' ', ''))
print(f"Seu nome em sem considerar os espaços tem {espaco} caracteres\n")
splita = nome.split()
lensplita = len(splita[0])
print(f"A quantidade de letras no seu primeiro nome é {lensplita}")

