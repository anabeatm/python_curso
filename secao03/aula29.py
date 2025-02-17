"while - qual letra aparece mais vezes?"

frase = 'Python é uma linguagem de programação'\
    'Multiparadigma'\
    'Python foi criado por guido van rossum.'.lower()

# print(frase.count("python"))

index = 0
apareceu_Mais_Vezes = 0
letra_Apareceu_Mais_Vezes = ""

while(index < len(frase)):
    letra_Atual = frase[index]

    if(letra_Atual == ' '):
        index += 1
        continue

    qnts_vezes_letraAtual_apareceu = frase.count(letra_Atual)

    if(apareceu_Mais_Vezes < qnts_vezes_letraAtual_apareceu):
        apareceu_Mais_Vezes = qnts_vezes_letraAtual_apareceu
        letra_Apareceu_Mais_Vezes = letra_Atual

    index += 1

print(
    f"A letra que apareceu mais vezes é '{letra_Apareceu_Mais_Vezes}' "
    f"e ela apareceu {apareceu_Mais_Vezes} vezes."
)