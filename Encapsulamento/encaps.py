'''
public , procted , private 


convenções criadas 
_ fraca   privado/protected (public_)

__ forte privado(_NOMECLASS_nomeatributo)

'''

class BaseDeDados:
    def __init__(self):
        self.__dados = {}        #dicionario dados publico


    @property
    def dados(self):
        return self.__dados


    def inserir_clientes(self , id , nome ,):
      if 'clientes' not in self.__dados:
         self.__dados['clientes'] = {id: nome}
      else:
         self.__dados['clientes'].update({id: nome})


    
    def lista_clientes(self):
       for id , nome in self.__dados['clientes'].items():
          print(id , nome)


    def apaga_cliente(self , id):
       del self.__dados['clientes'][id]

       

bd = BaseDeDados()
bd.inserir_clientes(1 , 'Kiwda')
bd.inserir_clientes(2 , 'Angel')
print(bd.dados)

