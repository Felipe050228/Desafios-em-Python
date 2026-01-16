class Conta_Bancaria:
    def __init__(self, senha):
        self.__senha = senha

    def get_senha(self):
        return self.__senha

    def set_senha(self, nova_senha):
        if len(nova_senha) >= 5:
            self.__senha = nova_senha
        else:
            print("\nSenha muito curta!\n")


conta = Conta_Bancaria("\n01234\n")
print(conta.get_senha())

conta.set_senha("99999\n")
print(conta.get_senha())




