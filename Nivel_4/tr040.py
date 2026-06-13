class Animal:
    def fazer_som(self):
        pass # Método base genérico

class Cachorro(Animal):
    def fazer_som(self):
        return "Au Au!"

class Gato(Animal):
    def fazer_som(self):
        return "Miau!"

class Vaca(Animal):
    def fazer_som(self):
        return "Muuu!"

# Função que demonstra o polimorfismo
def emitir_barulho(animal):
    print(animal.fazer_som())

# Criando instâncias
dog = Cachorro()
cat = Gato()
cow = Vaca()

# O mesmo método se comporta de forma diferente dependendo do objeto!
emitir_barulho(dog)  # Saída: Au Au!
emitir_barulho(cat)  # Saída: Miau!
emitir_barulho(cow)  # Saída: Muuu!
