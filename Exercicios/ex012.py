#Faca um programa que leia o valor de um produto calcule o seu desconto e mostre na tela o valor do porduto com o desconto
preco = float(input('Preco do produto: R$'))

comDesconto = preco - (preco/100)*5

print('O produto que custava R$ {:.2f} na promossao com desconto de 5% custara {:.2f}'.format(preco, comDesconto))
