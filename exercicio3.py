class produto:
    def __init__(self, nome, preço, quantidade):
        self.nome = nome
        self.preço = preço
        self.quantidade = quantidade

p1 = produto("Banana", 5, 17)
p2 = produto("Nuke", 90000, 16)

valortotal = p1.preço * p1.quantidade + p2.preço * p2.quantidade

print("Valor total em estoque:", valortotal)



    