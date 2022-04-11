# Faca um programa que leia um nome de uma pessoa q diga se ela tem o 'Silva' no nome
nome = str(input('Informe o nome da pessoa: ')).strip() #eliminamos os espacos

print('Your name have Silva? {}'.format('silva' in nome.lower()))
