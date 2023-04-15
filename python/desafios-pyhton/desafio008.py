n = int(input('Digite um valor em metros: '))
km = n / 1000
hm = n / 100
dam = n / 10
dm = n * 10
cm = n * 100
mm = n * 1000
print('{} metros são: \n{} Milímetros\n{} Centímetros\n{} Decímetros\n{} Metros\n{} Decâmetros\n{} Hectômetros\n{} Kilômetros'.format(n, mm, cm, dm, n, dam, hm, km))

