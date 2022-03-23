# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dolares ela pode comprar
# Considere U$$ 1,00 = RS 4,86

din = float(input('Quando dinheiro possui: R$ '))

print('Voce pode comprar: U$$ {}'.format(din/4.86))
print('Voce pode comprar: EUR {}'.format(din/5.33))
