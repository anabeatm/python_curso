#Exemplo:
print(12, 34)
#print = função
#12, 34 = argumentos não-nomeados
#No terminal apresentará: 12 34, sendo o meio um espaço padrão.

#Exemplo:
print(12, 34, sep='-')
#No terminal: 12-34, substituindo o espaço ' ' por '-'.

#Exemplo:
print(12, 34, sep='-', end='##')
print(56, 78, sep='-')
#No terminal: 12-34##56-78\
print("Luiz \"Otavio") #escape
print(r"Luiz \"Otavio\"") #r
print(type('Otavio')) #função type