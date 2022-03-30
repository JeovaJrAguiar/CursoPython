# Criar um programa que leia um numero e mostre seu dobro, tripo e raiz quadrada
num = int(input('Digite um numero: '))

print('Dobro: {} \nTriplo: {} \nRaiz quadrada: {:.2f}'.format( num*2, num*3, pow(num,(1/2))))
