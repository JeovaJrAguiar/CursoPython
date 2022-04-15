# Desenvolva um programa que pergunte a distancia de uma viagem em Km. Calcule o preco da passagem, cobrando:
#   - R$ 0,50  por km para viagens ate 200km
#   - R$ 0,45 p viagens mais longas

dist = float(input('Distancia da viagem: '))

if dist <= 200:
    preco = dist * 0.50 
else:
    preco = dist * 0.45

print('Preco da passagem: R$ {:.2f}'.format(preco))