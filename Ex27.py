"""27.Faça um programa que leia o nome completo de uma pessoa,
mostrando em seguida o primeiro e o último nome separadamente."""

n = input("Digite seu nome completo:\n").strip()
lista = n.split()
print (f'O seu primeiro nome é: {lista[0]}')
print (f'O seu ultimo nome é:{lista[-1]}')



