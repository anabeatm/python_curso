"""
Iterando strings com while


! ! ! NÃO CONSEGUI RESOLVER ! ! !
"""

#       0123
nome = 'Meu nome'  # strings são Iteráveis
# 'nome = ' -> Define uma variável chamada nome que armazena a string.


tamanho_nome = len(nome) # Calcula o tamanho da string 'nome' 
# e armazena o resultado na variável 'tamanho_nome = '.


"""
! ! ! RESOLUÇÃO DO PROFESSOR ! ! !
"""

indice = 0 # Inicializa uma variável 'indice = ' com o valor 0, 
# que será usada para acessar cada letra da string 'nome'.

nova_string = '' # Inicializa uma nova string vazia chamada 'nova_string', 
# que será construída durante o loop.

while indice < tamanho_nome: #  Inicia um loop 'while' que continua 
# enquanto o 'indice' for menor que o 'tamanho_nome'.

    letra = nome[indice] # Obtém a letra da string 'nome' no índice atual (indice) 
# e a armazena na variável 'letra'.

    nova_string += f'*{letra}' # Concatena à 'nova_string' o asterisco 
# seguido pela letra obtida acima.

    indice += 1 #  Incrementa o valor de 'indice' para avançar para 
# a próxima letra na próxima iteração do loop.

# O loop continua até que todas as letras da string nome tenham sido processadas.

nova_string += '*' # Adiciona um asterisco adicional ao final da 'nova_string'.

print(nova_string)