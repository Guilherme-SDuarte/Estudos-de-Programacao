w = input('Digite uma frase: ')
print('Sua frase tem {} "as"'.format(w.count('a')))
wd = w.split()
wa = wd[0]
wal = wd
print('O primeiro "a" aparece na casa {}'.format(wa.find('a')))
