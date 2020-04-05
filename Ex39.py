from datetime import date
"""Faça um programa que leia o ano de nascimento de um jovem e informe,
de acordo com sua idade:

- Se ele ainda vai se alistar ao serviço militar.
- Se é a hora de se alistar.
- Se já passou do tempo do alistamento.

Seu programa também deverá mostrar o tempo que falta ou que passou do prazo."""
anoatual=date.today().year
ano = int(input("Digite o ano de seu nascimento:\n"))
idade = anoatual-ano
print(f"Você nasceu em {anoatual-idade}, e atualmente tem {idade} anos")
if idade==18:
    print("É hora de se alistar")
elif idade > 18:
        print(f"Ja passou {idade-18} de você se alistar, o que está esperando?")
elif idade < 18:
        print(f"Ainda faltam {18-idade} anos para você se alistar!")

input()
