"""
Faça um programa que peça ao usúario para digitar um número inteiro, informe se este número é par ou ímpar.
Caso o usuário não digite um número inteiro, informe que não é um número inteiro.
"""

try:

# O bloco 'try' é onde colocamos o código que queremos executar, mas que pode gerar uma exceção. 
# Neste caso, colocamos o código que tenta converter a entrada do usuário em um número inteiro.

    num = int(input('Digite um número inteiro: '))
    
    if(num % 2 == 0):
        print('Esse número é par.')
    elif(num % 2 != 0):
        print('Esse número é ímpar.')

except ValueError:

#  O bloco 'except' é onde especificamos qual tipo de exceção queremos lidar. 
# Aqui, usamos 'except ValueError:' para lidar especificamente com a exceção 'ValueError', 
# que é lançada quando há um problema de conversão de tipo.

    print('Isso não é um número inteiro.')

"""
> Alternativa do Professor

if entrada.isdigit():
    entrada_int = int(entrada)
     par_impar = entrada_int % 2 == 0
     par_impar_texto = 'ímpar'

     if par_impar:
         par_impar_texto = 'par'

     print(f'O número {entrada_int} é {par_impar_texto}')
 else:
     print('Você não digitou um número inteiro')
"""