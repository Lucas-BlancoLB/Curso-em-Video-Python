# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela
# a sua porção inteira. Ex: Dgite um número: 6.127 o número 6.127 tem a parte inteira 6

# primeira tentativa com import

from math import trunc
n = float(input('Digite um número: '))
print(f'Seu número: {n}\nParte inteira: {trunc(n)}')

# Vou diminuir as linhas tirando o importe

# v = float(input('Digite um número: '))
# print(f'Seu número: {v} \nParte inteira: {v:.0f}')
