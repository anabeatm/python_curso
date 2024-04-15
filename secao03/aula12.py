# and == e
# Todas as condições precisam ser verdadeiras.
# Se qualquer valor for considerado falso, a espressão inteira será
# avaliada naquele valor.

entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Senha: ')

senha_permitida = '123456'
if(entrada == 'E' and senha_digitada == senha_permitida):
	print('Entrar')
else:
	print('Sair')
	
# São considerados valores falsy: 0, 0.0, '', False
# Também existe o tipo None que é usado para representar um não-valor

# Avaliação de curto circuito:
print(True and False and True)
print(True and 0 and True)