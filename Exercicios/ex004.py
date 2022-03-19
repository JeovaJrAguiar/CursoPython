# Faça um programa que leia algo pelo teclado e motre na tela seu tipo primitivo e todas as informações possíveis sobre ele
x = input('Escreva algo: ')
print('')

print('O tipo primitivo eh: ', type(x))
print('Soh tem espacos: ', x.isspace())
print('Eh um numero: ', x.isnumeric())
print('Eh alfabetico: ', x.isalpha())

print('Eh alfanumerico: ', x.isalnum())
print('Esta em maiusculas: ', x.isupper())
print('Esta em minusculas: ', x.islower())
print('Esta capitalizada: ', x.istitle())
