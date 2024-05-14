"""Calculadora com while feito por mim"""


while True:
    primeiro_num = float(input('Insira o primeiro número: '))
    segundo_num = float(input('Insira o segundo número: '))
    operador = input('Insira o operador [+, -, *, /]: ')
    if(operador == '+'):
        soma = primeiro_num + segundo_num
        print(soma)

    elif(operador == '-'):
        subtr = primeiro_num - segundo_num
        print(subtr)

    elif(operador == '*'):
        multi = primeiro_num * segundo_num
        print(multi)

    elif(operador == '/'):
        # divisao, _ = divmod(primeiro_num, segundo_num)
        divisao = primeiro_num / segundo_num
        print(divisao)

    sair_ouNao = input('Deseja sair? [s/n]: ').lower()
    if sair_ouNao == 's':
        break