# DESAFIO Faça um algoritmo que leia o preço de um produto e mostre o seu novo preço,
# com 5% de desconto.

# Digite o valor sem R$ ou $. Não use vírgula, use ponto no lugar
p = float(input('Antigo preço: '))
d = p / (1/0.05)
vd = p - d
print('Novo preço:', vd)
