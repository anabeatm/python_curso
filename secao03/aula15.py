# Operadores in e not in
# Strings são iteráveis
#  0 1 2 4 5 6
#  O t á v i o
# -6-5-4-3-2-1
nome = 'Otávio'
print(nome[2])
print(nome[-4])

print('á' in nome) # verifica se 'á' está(in) na variável 'nome'
print('vio' not in nome) # verifica se 'vio' está na variável 'nome'
# se estiver(not in), ele nos retornará False

nome = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if(encontrar in nome):
	print(f'{encontrar} está em {nome}.')
else:
	print(f'{encontrar} não está em {nome}.')
