"""25. Crie um programa que leia o nome deuma pessoa e diga se ela
tem "SILVA" no nome."""

n = input("Digite o nome completo de uma pessoa:")
if n.find('silva') != -1:
    print("Tem silva no nome")
else:
    print("Não tem silva no nome")
