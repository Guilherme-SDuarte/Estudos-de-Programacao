from math import hypot
n = float(input('Cateto oposto: '))
n1 = float(input('Cateto adjacente: '))
hi = hypot(n, n1)
print('A hipotenuza vale {:.2f}'.format(hi))
