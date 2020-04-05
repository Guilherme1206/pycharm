from datetime import date
"""A confederação Nacional de Natação precisa de um programa
que leia o ano de nascimento de um atleta e mostre
sua categoria, de acordo com a idade:

-Até 9 anos: MIRIM
-Até 14 anos: INFANTIL
-Até 19 anos: JUNIOR
-Até 20 anos: SENIOR
-Acima: MASTER"""
anoatual=date.today().year
ano = int(input("Digite o ano de seu nascimento:\n"))
idade = anoatual-ano

if idade <= 9:
    print(f"O atleta possui {idade} anos, esta na categoria MIRIM")
elif idade > 9 and idade <= 14:
    print(f"O atleta possui {idade} anos, esta na categoria INFANTIL")
elif idade > 14 and idade <= 19:
    print(f"O atleta possui {idade} anos, esta na categoria JUNIOR")
elif idade==20:
    print(f"O atleta possui {idade} anos, esta na categoria SÊNIOR")
else:
    print(f"O atleta possui {idade} anos, esta na categoria MASTER")


input()
