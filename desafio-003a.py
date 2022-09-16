# n1 = input('Insira um número: ')
# n2 = input('Insira mais um número: ')
# print('A soma do primeiro com o segundo é ', n1 + n2)

# A soma do primeiro mas o segundo esta errada, resultado fica n1n2 e nao n1+n2.
# Minha solução sem ver o vídeo.

# n1 = input('Insira um número: ')
# n2 = input('Insira mais um número: ')
# soma = n1 + n2
# print('A soma do primeiro com o segundo é ', soma)

# LULW deu errado, Continua juntando e não soma.

# Solução para o erro de soma. Tipo primitivo int()
# Agora os N não concatenam
n1 = int(input('Insira um número: '))
n2 = int(input('Insira mais um número: '))
soma = n1 + n2
print('A soma do primeiro com o segundo é', soma)

# print interessante é usar o .format ou f' com {}
# Evita o uso da vírgula

print(f'A soma do primeiro com o segundo é {soma}')

