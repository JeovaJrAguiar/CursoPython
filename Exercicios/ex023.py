# Faca um programa que tenha ate 4 digitos e mostre cada um dos digitos separados
num = int(input('Informe o numero: '))

print('Unidade: {}'.format(num // 1 % 10))
print('Dezena: {}'.format(num // 10 % 10))
print('Centena: {}'.format(num // 100 % 10))
print('Milhar: {}'.format(num // 1000 % 10))
