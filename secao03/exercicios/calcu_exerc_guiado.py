""" Calculadora com while feito pelo professor """


while True:

    numero_1 = input('Digite um número: ')
    numero_2 = input('Digite outro número: ')
    operador = input('Digite o operador (+-/*): ')

    numeros_validos = None

    try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
        numeros_validos = True
    except:
        numeros_validos = None

    if numeros_validos is None:
        print('Um ou ambos os números digitados são inválidos.')
        continue

    operadores_permitidos = '+-/*'

    if operador not in operadores_permitidos:
        print('Operador inválido.')
        continue

    if len(operador) > 1:
        print('Digite apenas um operador.')
        continue

    if(operador == '+'):
        soma = num_1_float + num_2_float
        print(soma)

    elif(operador == '-'):
        subtr = num_1_float - num_2_float
        print(subtr)

    elif(operador == '*'):
        multi = num_1_float * num_2_float
        print(multi)

    elif(operador == '/'):
        # divisao, _ = divmod(num_1_float, num_2_float)
        divisao = num_1_float / num_2_float
        print(divisao)

    sair = input('Quer sair? [s]im: ').lower().startswith('s')

    if sair is True:
        break

"""
! ! !Explicação detalhada! ! !

1. O programa está dentro de um loop `while True`, o que significa que 
continuará executando até que seja explicitamente interrompido com uma 
instrução `break`.

2. Dentro do loop, o programa solicita ao usuário que insira dois 
números (`numero_1` e `numero_2`) e o operador matemático (`operador`) 
que deseja utilizar.

3. Uma variável `numeros_validos` é inicializada como `None`.

4. É feita uma tentativa (`try-except`) de converter os números inseridos 
pelo usuário em números de ponto flutuante (float). Se a conversão 
for bem-sucedida, a variável `numeros_validos` é definida como `True`, 
caso contrário, permanece `None`.

5. Se os números inseridos não forem válidos (ou seja, a conversão falhou), 
uma mensagem de erro é exibida e o loop continua com a próxima iteração.

6. Em seguida, o programa verifica se o operador inserido pelo usuário está 
entre os operadores permitidos (+, -, *, /). Se não estiver, 
uma mensagem de erro é exibida e o loop continua.

7. O programa verifica se o comprimento do operador inserido 
é maior que 1 (ou seja, se o usuário inseriu mais de um caractere). 
Se for, uma mensagem de erro é exibida e o loop continua.

8. Se todas as verificações anteriores forem bem-sucedidas, 
o programa realiza a operação matemática correspondente com base 
no operador inserido pelo usuário. Ele realiza uma das quatro 
operações matemáticas: adição, subtração, multiplicação ou divisão.

9. Após realizar a operação, o resultado é exibido na saída padrão.

10. O programa então pergunta ao usuário se deseja sair. 
Se o usuário inserir 's' ou 'sim', o loop é interrompido usando a 
instrução `break`, caso contrário, o loop continua com a próxima iteração.
"""