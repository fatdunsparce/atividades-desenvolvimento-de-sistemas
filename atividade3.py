def fatorial(numero2):
    if numero2 == 0:
        return 1
    else:
        return numero2 * fatorial(numero2-1)

numero2 = int(input("Digite um número:"))
result = fatorial(numero2)
print("A fatorial de", numero2, "é:", result)