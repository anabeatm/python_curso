"""

Interpolação básica de strings
s - string
d e i - int
f - float
x e X - hexadecimal (ABCDEF0123456789)

"""

nome = 'Luiz'
preco = 1000.958938
variavel = 'Luiz, o preço total foi de R$1000.95'
variavelDois = '%s, o preço total foi de R$%.2f' % (nome, preco)
print(variavel)
print('O hexadecimal de %d é %04x' % (15, 15))
