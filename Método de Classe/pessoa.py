class Pessoa:
    ano_atual = 2019


    def __init__(self , nome , idade):
        self.nome = nome
        self.idade = idade
        pass

    def get_ano_nascimento(self):
        print(self.ano_atual - self.idade)



p1 - Pessoa('Luiz', 32)
print(Pessoa.ano_atual)