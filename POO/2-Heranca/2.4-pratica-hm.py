# 2.4 - Prática de Herança Múltipla


# Classe Avó
class Animal:
    def __init__(self, nro_patas):
        self.nro_patas = nro_patas
    
    def __str__(self) -> str: # Este método especial será executado quando uma instância do objeto for printada (Stringificada)
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}" # List Comprehension




# Classes Mães
class Ave(Animal):
    def __init__(self, cor_bico, **kw):
        super().__init__(nro_patas=kw["nro_patas"])
        self.cor_bico = cor_bico


class Mamifero(Animal):
    def __init__(self, cor_pelo, **kw): # Utiliza-se Kwargs para que o interpretador não confunda o número de parametros das classes.
        super().__init__(nro_patas=kw["nro_patas"])
        self.cor_pelo = cor_pelo


# Classes Filhas
class Cachorro(Mamifero):
    pass


class Gato(Mamifero):
    pass


class Leao(Mamifero):
    pass


class Ornitorrinco(Mamifero, Ave):
    pass


#                                                   Instâncias
gato_felix = Gato(4,'Preto')
print(gato_felix, '\n')

agente_perry = Ornitorrinco(4, 'Verde', 'Laranja')
print(agente_perry, '\n')