"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário descrito, exiba a saudação apropriada. Ex:
Bom dia 0-11; Boa-tarde 12-17; Boa-noite 18-23.
"""
try:
    hora_do_dia = int(input('Que horas é agora? (0-23) '))

    if(hora_do_dia >= 0 and hora_do_dia <= 11):
        print('Bom dia!')
    elif(hora_do_dia >= 12 and hora_do_dia <= 17):
        print('Boa tarde!')
    elif(hora_do_dia >= 18 and hora_do_dia <= 23):
        print('Boa noite!')

except ValueError:
    print('Valor incorreto. Insira um valor inteiro de 0 à 23.')


"""
> Alternativa do Professor

entrada = input('Digite a hora em números inteiros: ')

try:
    hora = int(entrada)

    if hora >= 0 and hora <= 11:
        print('Bom dia')
    elif hora >= 12 and hora <= 17:
        print('Bom tarde')
    elif hora >= 18 and hora <= 23:
        print('Bom noite')
    else:
        print('Não conheço essa hora')
except:
    print('Por favor, digite apenas números inteiros')
"""