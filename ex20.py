import random
a1 = input("Digite o nome do primeiro aluno:\n")
a2 = input("Digite o nome do segundo aluno:\n")
a3 = input("Digite o nome do terceiro aluno:\n")
a4 = input("Digite o nome do quarto aluno:\n")
lista=[a1,a2,a3,a4]
rdn = random.sample(lista,4)
print(f"A ordem escolhida é: {rdn}")
