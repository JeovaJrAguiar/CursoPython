# Crie um algoritimo que leia um valor em metros e o exiba convertido em centimetros e milimetros.
# km hm dam m dm cm mm
medida = float('distancia em metros: ')

km = medida / 1000
hm = medida / 100
dam = medida / 10
dm = medida * 10
cm = medida * 100
mm = medida * 1000

print(''.format(mm, cm, dm, dam))
