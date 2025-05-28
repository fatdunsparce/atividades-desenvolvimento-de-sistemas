class ContaBancaria:
    def __init__(self, saldo=0):
        self.saldo = saldo


    def depositar(self, valor):
        self.saldo += valor  # Adiciona valor ao saldo


    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor  # Subtrai valor do saldo
        else:
            print("Saldo insuficiente")


conta = ContaBancaria(100)
conta.depositar(50)
conta.sacar(30)
print(conta.saldo)  # Saída: 120
