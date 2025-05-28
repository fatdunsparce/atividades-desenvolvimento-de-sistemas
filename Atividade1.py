class aluno:
    def __init__(self, nome, matrícula, curso):
        self.nome = nome
        self.matrícula = matrícula
        self.curso = curso

    def exibirdados(self):
        return self.nome, self.matrícula, self.curso
    
a1 = aluno("Maria", 16726, "Banco de Dados")
a2 = aluno("Otávio", 21562, "Ciencias da Computação")

print(a1.exibirdados())