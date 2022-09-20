# DESAFIO Faça um programa que converta temperaturas em escalas diferentes
t = float(input(f'Conversor de temperatura em Celsios: '))
f = t / 5 * 9 + 32
k = t + 273.15
print(f'{f:.2f}º Fahrenheit')
print(f'{k:.2f} Kelvin')

# alinhei os valores minimos com o google celsius to kelvin 0 = -273.15
