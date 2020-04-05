km = float(input("Quantos km foram percorridos?\n"))
dias = int(input("Por quantos dias ele foi alugado?\n"))
carro = (60*dias) + (0.15*km)
print (f"A quantidade de km é {km}, a quantidade de dias é {dias} e \
o valor final é R$ {carro:.2f}")
