# Crie um algoritmo que receba um numero e mostre o seu doblo, triplo e raiz quadrada.
n = int(input('digite um numero:'))

print('O dobro: {} \nTriplo: {} \nRaiz Quadrada: {:.2f}'.format(n*2, n*3, pow(n,1/2)))
