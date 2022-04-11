# Faca um programa que leia a velocidade de um carro.Se ele ultrapassar 80km/h mostre uma mensagem dizendo que ele foi multado. A multa cai custar 7,00 Rs para cada km amida do limite

velocidade = float(input('Qual a velocidade: '))

if velocidade > 80:
    print('Multado! Voce ultrapassou o limite da via!')
    print('Voce deve pagar um multa de {:.2f}!'.format(7 * (velocidade - 80)))
    print('Tenha um bom dia! Dirija com seguranca!')
