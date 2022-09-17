# teste operadores aritiméticos

n1 = int(input('Digite um número: '))
n2 = int(input('Digite um número: '))

# Por ordem de menor a maior importancia

# Operadores de adição e subtração
a = n1 + n2
s = n1 - n2

# Operadores de multipicação e divisão simples
# dexata | (//) é o valor da divisão exata
# dresto | (%)  é o valor do resto da divisão
m = n1 * n2
d = n1 / n2
dexata = n1 // n2
dresto = n1 % n2

# Operador de Potencia e a Raiz (inverso da potência)
# pow() a função da multipicação | pow(base,multipicador, modulo)
M = n1 ** n2
R = pow(n1, n2)**(1/2)

# Maxima prioridade no calculo aritimético
P = (n1+n2)

print(f'Soma e subitração: {a} & {s} ')
print(f'Multiplicação e divisão comum: {m} & {d}')
print(f'divisão exata  e resto da divisão: {dexata} & {dresto}')
print(f'Potência e Raiz: {M} & {R}')
print(f'parênteses com soma: {P}')
