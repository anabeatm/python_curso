contador = 0

while contador <= 10:
	contador += 1
	
	if contador == 6:
		print('Não vou mostrar o 6.')
		continue
	
	if contador >= 10 and contador <= 27:
		print('Comi o', contador, ' :P')
		continue
	
	
	
	print(contador)
	
	
	if contador == 40:
		break
	

print('Acabou.')