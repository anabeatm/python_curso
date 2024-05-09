"""
CONSTANTE = 'Variáveis' que não vão mudar muitas condições no mesmo if (ruim)
	<- Contagem de complexidade (ruim)
"""
velocidade = 61 # velocidade atual do carro
local_carro = 90 # local em que o carro está na estrada

RADAR_1 = 60 # valocidade máxima do radar 1
LOCAL_1 = 100 # local onde o radar 1 está
RADAR_RANGE = 1 # a distância onde o radar pega

if RADAR_1 <= velocidade:
	print('passou do limite.')
if local_carro >= (LOCAL_1 - RADAR_RANGE) and \
		local_carro <= (LOCAL_1 + RADAR_RANGE) and \
			RADAR_1 <= velocidade:
	print('carro multado em radar 1.')
	
# lógica mais compreensível

velocidade_carro_passou_radar__1 = velocidade > RADAR_1
carro_passou_radar_1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and \
    local_carro <= (LOCAL_1 + RADAR_RANGE)
carro_multado_radar_1 = carro_passou_radar_1 and velocidade_carro_passou_radar__1
		
if carro_passou_radar_1:
    print('carro passou no radar 1')

if carro_multado_radar_1:
    print('carro multado no radar 1')
