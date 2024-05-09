"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou menos, escreva 'Seu nome é curto';
se tiver entre 5 a 6 letras, escreva 'Seu nome é normal.'; maior que 6 letras, escreva 'Seu nome é grande.'
"""
nome = input('Escreva seu nome: ')
contar_nome = len(nome)

print(f'Seu nome é {nome} e tem {contar_nome} caracteres - contando os espaços - .')

if(contar_nome <= 4):
    print('Ou seja, seu nome é curto.')
elif(contar_nome >= 5 and contar_nome <= 6):
    print('Ou seja, seu nome é médio.')

else:
    print('Ou seja, seu nome é grande.')


"""
> Alternativa do Professor

nome = input('Digite seu nome: ')
tamanho_nome = len(nome)

if tamanho_nome > 1:
    if tamanho_nome <= 4:
        print('Seu nome é curto')
    elif tamanho_nome >= 5 and tamanho_nome <= 6:
        print('Seu nome é normal')
    else:
        print('Seu nome é muito grande')
else:
    print('Digite mais de uma letra.')
"""