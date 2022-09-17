# DESAFIO Faça um programa que leia a largura e a altura de uma parede em metros,
# calcule a sua área e a quantidade de tinta necessária para pintá-la,
# sabendo que cada litro de tinta, pinta uma área de 2m².

l = int(input('Largur em metros: '))
a = int(input('Altura em metros: '))
ar = l * a
L = ar // 2
print(f'Para {ar} m² de área, é necessario {L} L de tinta.')