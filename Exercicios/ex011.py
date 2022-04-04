#Faca um programa que leia a largura e a altura de uma parede em metros, calcule a sua area e a quantidade de tinta nescessaria para pinta-la, sabendo que cada litro de tinta pinta 2 metros quadrados.

lar = float(input("Digite a largura da parede: "))
alt = float(input("Digite a altura da parede: "))

area = lar * alt

print("Sua parede tem dimensão: {:.2f} x {:.2f}".format(lar, alt, area))
print("Sua parede tem área: {:.3f}".format(area))
print("Para pintar sua parede, precisa-ra de {:.3f} litros de tinta".format(area/2))