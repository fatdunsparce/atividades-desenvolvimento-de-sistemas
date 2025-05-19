def verificarimparpar(Numero):
    if Numero % 2 == 0:
        return "par"
    else:
        return "impar"

Numero = int(input("Digite um número:"))
resultado = verificarimparpar(Numero)
print("o numero", Numero, "é", resultado)