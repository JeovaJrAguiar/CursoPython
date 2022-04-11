# Faca um programa que leia um nome de uma cidade e diga se ela comeca ou nao com o nome 'santo'
cid = str(input('Informe o nome da cidade: ')).strip() #eliminaos os espacos

#verificamos os 5 primeiros caracteres do vetor

print(cid[:5].upper() == 'SANTO')
