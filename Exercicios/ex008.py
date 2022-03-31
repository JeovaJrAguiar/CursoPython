# Crie um algoritimo que leia um valor em metros e o exiba convertido em centimetros e milimetros.
# km hm dam m dm cm mm
medida = float(input('Distancia em metros: '))

km = medida / 1000
hm = medida / 100
dam = medida / 10
dm = medida * 10
cm = medida * 100
mm = medida * 1000

#print('Km: {:.4f}'.format(km))
print('Km: {:.4f}\nHm: {:.4f}\nDam: {:.4f}\nDm: {:.4f}\nCm: {:.4f}\nMm: {:.4f}'.format(km, hm, dam, dm, cm, mm))
