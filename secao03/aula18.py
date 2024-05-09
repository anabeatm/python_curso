"""
Fatiamento de string
 012345678
 Olá mundo
-987654321
Fatiamento [i:f:p] [::]
Obs.: a função len retorna a qtd de caracteres da str
"""

variavel = 'Olá mundo'
print(variavel[-4])
print(variavel[4:]) # '4' é o inicio e após o ':' é o final.
print(variavel[4:8])
print(variavel[:5])
print(variavel[-8:-2])

# função len CONTA os caracteres de uma string
print(len(variavel))

print(variavel[0:9:2])
print(variavel[::-1]) # inverte
