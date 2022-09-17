# DESAFIO Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos
# Dólares ela pode comprar. CONSIDERE US$1.00 = R$3.27

d = float(input('Valor de dinheiro: '))
c = d // 3.27
print(c)

# // nao aceita 327, tenho que por 328
# / converte valores menores que 3.27, divisão 327 da certo
# 327 % 3.27 Resta 3.2699999999999982

