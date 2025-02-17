"while/else"

string = "Valor qualquer"

i = 0
while(i < len(string)):
    letra = string[i]

    print(letra)
    i += 1

# onde o else entra
else:
    print("O else foi executado.")

# o else só acontecerá se o while for completado corretamente
# sem forçar uma interrupção

print("Fora do while.")

# se ocorrer de ter um "break" no laço, "else" não será executado