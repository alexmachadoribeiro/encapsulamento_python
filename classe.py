# classe
class Pessoa:
    def __init__(self, nome, idade, email):
        self.__nome = nome
        self.__idade = idade
        self.__email = email
    
    # método get nome
    @property
    def nome(self):
        return self.__nome
    
    # método set nome
    @nome.setter
    def nome(self, nome):
        self.__nome = nome
    
    @property
    def idade(self):
        return self.__idade
    
    @idade.setter
    def idade(self, idade):
        self.__idade = idade

    @property
    def email(self):
        return self.__email
    
    @email.setter
    def email(self, email):
        self.__email = email