# Crie um programa que leia o nome completo de uma pessoa e mostre
# - O nome com todas as letras maiuscilas e minusculas.
# - Quantas letras ao todo(sem considerar espacos).
# - Quantas letras tem o primeiro nome.

nome = str(input('Seu nome: ')).strip()
#nomeQuebrado = nome.str
print('Nome em maiusculas: {}'.format(nome.upper()))
print('Nome em maiusculas: {}'.format(nome.lower()))

print('Quantidade de letras ao todo: {}'.format(len(nome) - nome.count(' ')))
#nome.find() -- busca onde fica o primeiro caracter
#print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))

separa = nome.split() #vai separar a string em uma lista
print(separa)
