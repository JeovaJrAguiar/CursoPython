# Faca um programa que leia um nome completo de uma pessoa e mostre em seguida o primeiro e ultimo noem separadamente

n = str(input('Digite o nome completo: ')).strip()
nome = n.split()
print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu primeiro nome é {}'.format(nome[len(nome) - 1]))
