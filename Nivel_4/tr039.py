class Bliblioteca:
    def __init__(self):
        self.livros = []
        self.usuario = []
class Livraria:
    def __init__(self,titulo,autor,startos=True):
        self.titulo = titulo
        self.autor = autor
        self.startos = startos

    def disponivel(self,):
        if self.startos == True:
            print(f'\nO livro ({self.titulo}) de  ({self.autor}) esta disponivel\n')
        else:
            print(f'\nO livro ({self.titulo}) de ({self.autor}) não esta disponivel\n')


class Conta_do_Usuario:
    def __init__(self,nome,idade,ID_usuario):
        self.nome = nome
        self.idade = idade
        self.ID_usuario = ID_usuario