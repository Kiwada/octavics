class Pessoa:
    ano_atual = 2019


    def __init__(self , nome , idade):
        self.nome = nome
        self.idade = idade
        pass

    def get_ano_nascimento(self):
        print(self.ano_atual - self.idade)

    @classmethod #para saber quando ultilizar um método de classe ou de instáncia é so pensar se o método que estou criando é relacionado à classe em geral ao molde em geral ou a instancia 
    def por_ano_nascimento(cls , nome , ano_nascimento):
        idade = cls.ano_atual - ano_nascimento  
        return cls(nome, idade) #cls se refere a classe PESSOA
       



p1 = Pessoa.por_ano_nascimento('Luiz' , 1987)
print(p1)
print(p1.nome , p1.idade)
print(p1.idade)
p1.get_ano_nascimento()