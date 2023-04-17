from math import radians, sin, cos, tan
an = float(input('Digite o ângulo que você deseja: '))
seno = sin(radians(an))
cosseno = cos((radians(an)))
tan = tan(radians(an))
print('O ângulo de {}º tem: \nO SENO de {:.2f}º \nO COSSENO de {:.2f}º \nA Tangente de {:.2f}º'.format(an, seno, cosseno, tan))