# Crie um programa que leia um numero real qualquer pelo teclado e mostre na tela a sua porçao inteira
from math import trunc
num = float(input('Digite um valor: '))
print('A parte inteira do numero e {}'.format(trunc(num)))
