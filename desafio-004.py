 # DESAFIO Fasa um programa qua leia algo pelo teclado e mostre na tela o seu tipo primitivo
 # e todoas as informações possíveis sobre ela

# Diz se o num é alfanumerico se tem espaço maiusculo ou minusculo, se for enter,
 # mas nn diz se for caracter especial.

var = input('Insira um valor: ')
print(var.isspace(), var.isnumeric(), var.isalnum(), var.islower(), var.isupper())

# False False False False False = ENTER
# True   --    --    --    --   = Espaço
# False True  True   --    --   = Númerico
#  --    --   True   --    --   = Palavra
#  --    --   True  True   --   = Letra + tudo minusculo
#  --    --   True  False True  = Letra + tudo MAIUSCULO
