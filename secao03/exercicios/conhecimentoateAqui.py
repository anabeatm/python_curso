"""
Exercício:

> Peça ao usuário para digitar seu nome - ok!
> Peça ao usuário para digitar sua idade - ok!
> Se nome e idade forem digitados:
	Exiba:
		>Seu nome é - ok!
		>Seu nome invertido é - ok!
		>Seu nome contém (ou não) espaços - ok!
		>Seu nome tem n letras - mais ou menos! - ok!
		>A primeira letra do seu nome é - ok!
		>A última letra do seu nome é - ok!
> Se nada for digitado em nome ou idade:
	>exiba 'Desculpe, você deixou campos vazios.' - ok!
"""

nome = input('Digite seu nome completo: ') #ok!
idade = input('Digite sua idade: ') #ok!

if(nome and idade): #não tão ok!
    print(f'Seu nome é {nome}.') #ok!
    print(f'Seu nome invertido é {nome[::-1]}.') #ok! # começa a contar negativamente o nome, exibindo-o invertido
    
    if(' ' in nome): #ok! # verifica se há espaços - logo que é um caractere ' ' - na variável nome
        print('Seu nome tem espaços.')
    else:
        print('Seu nome não tem espaços.')
    
    letras_contar = len(nome) #ok!
    print(f'Seu nome tem {letras_contar} letras.') #ok!
    primeiraLetra = nome[0] #ok!
    print(f'A primeira letra do seu nome é {primeiraLetra}.')
    ultimaLetra = nome[-1] #ok! # como quero saber o último caractere, faz sentido começar a contar ao contrário.
    # logo que não tem como saber quantos caractere pode ter um nome.
    print(f'A última letra do seu nome é {ultimaLetra}.')

else: #ok!
    print('Desculpe, você deixou campos vazios.')
