class aluno:
    def __init__(self, nome, turma, nota):
        self.nome = nome
        self.turma = turma
        self.nota = nota

a1 = aluno("Maria", "3Btds", 17)
a2 = aluno("João", "2Btds", 16)

print(a1.nome, a1.turma, a1.nota)
print(a2.nome, a2.turma, a2.nota)
