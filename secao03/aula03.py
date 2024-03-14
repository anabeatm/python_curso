#Exemplo
# print(1 + 1) #python entende que é uma operação matemática e soma os dois números int.
# print('a' + 'b') #python junta, retornando 'ab'. chamamos isso de polimorfismo, logo que o sinal + tem mais de uma função.
# print('1' + 1) # terminal dá erro, pois python não consegue juntar str ('1') com int (1), e nem fazer a soma.

print('1', type('1'))
print(int('1'), type(int('1'))) # class int() transforma str 1 para int 1.
print(int('1') + 1) # python entende a coersão e realiza a soma de int 1 com 1.