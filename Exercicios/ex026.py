# Faca um programa que leia uma frase pelo teclado e mostre
#   - Quantas vees aparece a letra 'A'
#    - Emq ue posicao ela aparece a primeira vez
#   - Em que posicao ela aparece a ultima vez
frase = str(input('Digite uma frase: ')).lower().strip()

print('A letra a aparece {} vezes'.format(frase.count('a')))
print('A primeira letra a apareceu na {} posicao'.format(frase.find('a') + 1))
print('A ultima letra a apareceu na {} posicao'.format(frase.rfind('a') + 1))
