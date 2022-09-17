nome = input('Qual o seu nome? ')

# dentro do .format nas chaves :N, N o numero de casas adicionais ao 'nome'. : o multiplicador
# dentro do .format nas chaves :>N ou :<N, > e < O  sentido das casas adicionais
# dentro do .format nas chaves :^N, ^ Centraliza 'nome' nas casas adicionais
# dentro do .format nas chaves :_^N, '_' entre : e a condicional ^, são preenchidas com '_'
print(f'Seja muito bem_vindo(a) |{nome}|')   # **Print(), Controle da teoria
print(f'Seja muito bem-vindo(a) |{nome :>10}|')
print(f'Seja muito bem-vindo(a) |{nome :<10}|')
print(f'Seja muito bem-vindo(a) |{nome :^10}|')
print(f'Seja muito bem-vindo(a) |{nome :_^10}|')

# end='' Junta a linha, quebra o print em dois, a msg continua na mesma linha
# end='' dentro das aspas é o que fica entre as duas linhas, ex end='___'; msg1___msg2
print(f'Espero que sejas muito bem atendido(a){nome}.', end=' ')
print(f'Pelo resto da semana da sua hospedagem{nome}!')

# outro ex com end=''
print('Hello', end=' ')
print('world')
