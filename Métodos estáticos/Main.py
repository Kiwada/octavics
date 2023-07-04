from random import randint


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
    


    @staticmethod  #não se ultiliza self *
    def gerar_id():
        rand = randint(10000 , 19999)  #variavel so vai estar disponivel dentro do escopo do static method
        return rand

    
       



p1 = Pessoa.por_ano_nascimento('Luiz' , 1987)
print(p1.gerar_id())