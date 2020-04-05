"""Elabore um programa que calcule o valor a ser pago por um produto,
considerando o seu preço normal e condição de pagamento:

-À vista dinheiro/cheque: 10% de desconto
-À vista no cartão: 5% de desconto
-em até 2x no cartão: preço normal
-3x ou mais no cartão: 20% de juros"""

valor = float(input("Digite o valor a ser pago pelo produto:\n"))
pagamento = int(input("Digite a forma de pagamento:\n\
Digite [1] para pagamento a vista no dinheiro/cheque\n\
Digite [2] para pagamento a vista no cartão\n\
Digite [3] para pagamento parcelado em até 2x no cartão\n\
Digite [4] para pagamento parcelado em 3x ou mais no cartão\n"))

if pagamento == 1:
    print(f"O desconto para pagamento a vista no dinheiro/cheque\n\
será de R$ {valor-valor*0.9:.2f} e o total a pagar será de R$ {valor*0.9:.2f}")
elif pagamento == 2:
    print(f"O desconto para pagamento a vista no cartão\n\
será de R$ {valor-valor*0.95:.2f} e o total a pagar será de R$ {valor*0.95:.2f}")
elif pagamento == 3:
    print(f"O total a pagar em até 2x no cartão será de R$ {valor:.2f}")
elif pagamento == 4:
    print(f"O juros para pagamento em 3x ou mais no cartão\n\
será de R$ {valor * 1.2 - valor:.2f} e o total a pagar será de R$ {valor * 1.2:.2f}")
else:
    print("Tente novamente")
input()