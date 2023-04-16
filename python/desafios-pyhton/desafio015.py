d = float(input('Quantos dias alugados? '))
km = float(input('Quantos Km rodados? '))
da = d * 60
kmr = km * 0.15
print('O valor que deve ser pago é de R${:.2f}'.format(da + kmr))
