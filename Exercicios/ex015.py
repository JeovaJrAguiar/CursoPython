# Escreva um programa que recebe a quantidade de km alugados por um carro e a quantidade de dias pelos quais foi alugado. calculeo preco a pagar, sabendo que o carro custa R$ 60 por dia e R$ 0,15 por km rodado
dias = float(input('Quantos dias o carro foi alugado: '))
km = float(input('Quantos km foram rodados: '))

preco = float((dias * 60) + (km * 0.15))

print('Total a pagar: R$ {:.2f}'.format(preco) )
