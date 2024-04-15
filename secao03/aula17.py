# Formatação básica de strings
# s - string
# d - int
# f - float
# .<número de dígitos>f
# x ou X - Hexadecimal
# (Caractere)(><^)(quantidade)
# > - esquerda
# < - direita
# ^ - centro 
# = - força o número a aparecer antes dos zeros
# Sinal - + ou -
# Ex.: 0>-100, .1f
# Conversion flags - !r !s !a

variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10.}')
print(f'{variavel: <10.}')
print(f'{variavel: ^10.}')
print(f'{1000.4763846238:0=+10,.1f}')
print(f'O hexadecimal de 1500 é {1500:04x}')
print(f'{variavel!r}')
