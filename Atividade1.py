class produto:
    def __init__(self):
        self.__preço = None

    def mostrarpreço(self):
        return self.__preço

    def definirpreço(self, p):
        if p > 0:
            self.__preço = p
        else:
            raise ValueError("Preço deve ser maior que 0")

p1 = produto()
p2 = produto()

p1.definirpreço(0)
p2.definirpreço(20)

print(p1.mostrarpreço())
print(p2.mostrarpreço())