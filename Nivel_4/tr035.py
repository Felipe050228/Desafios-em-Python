class NotasBimestrais:
    def __init__(self, nome):
        self.nome = nome
        self.notas = []

    def adicionar_nota(self, nota):
        self.notas.append(nota)

    def mostrar_notas(self):
        print(f'\nNotas do aluno {self.nome}:')
        for i, nota in enumerate(self.notas, start=1):
            print(f'{i}º bimestre: {nota}')

    def calcular_media(self):
        media = sum(self.notas) / len(self.notas)
        return media

print('==' * 20)
print('   vamos calcular sua nota bimestral')
print('==' * 20)

aluno = input('\nDigite seu nome: ').capitalize()
aluno1 = NotasBimestrais(aluno)

for i in range(4):
    nota = float(input(f'Digite a nota do {i+1}º bimestre: '))
    aluno1.adicionar_nota(nota)

aluno1.mostrar_notas()

media = aluno1.calcular_media()
print(f'\nMédia final: {media:.2f}')

if media >= 6:
    print('Situação: APROVADO ✅')
else:
    print('Situação: REPROVADO ❌')
