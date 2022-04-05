
# Crie um programa que leia um cangulo qualquer e mostre na tela o valor do seco, cosseno e tangente desse angulo
from math import radians, sin, cos, tan

an = float(input('Digite o angulo: '))

seno = sin(radians(an))
cos = cos(radians(an))
tan = tan(radians(an))

print('Seno: {:.2f}'.format(seno))
print('Seno: {:.2f}'.format(cos))
print('Seno: {:.2f}'.format(tan))
