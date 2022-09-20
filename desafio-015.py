# DESAFIO Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado
# e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

d = float(input('Quantidade de Km percorrido: '))
a = int(input('Quantos dias alugados: '))
print(f'A pagar R${a*60} e R${d*0.15:.2f} \nValor   total  R${a*60+d*0.15:.2f} ')
