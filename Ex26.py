"""26: Faça um programa que leia uma frase pelo teclado e mostre quantas
vezes aparece a letra "A", em que posição ela aparece a primeira vez
e em que posição ela aparece a última vez."""

n = input("Digite uma frase:\n").upper().strip()
print (f'A letra a aparece {n.count("A")} vezes')
print(f'A primeira letra a aparece na posição {n.find("A")+1}')
print(f'A ultima letra a aparece na posição {n.rfind("A")+1}')

