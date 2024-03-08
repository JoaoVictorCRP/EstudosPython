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
        super().__init__(**kw)
        self.cor_bico = cor_bico


class Mamifero(Animal):
    def __init__(self, cor_pelo, **kw): # Utiliza-se Kwargs para que o interpretador não confunda o número de parametros das classes.
        self.cor_pelo = cor_pelo
        super().__init__(**kw)


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
gato_felix = Gato(cor_pelo='Preto', nro_patas=4) # Lembrando: Quando incluimos kwargs devemos nomear todos os parametros.
print(gato_felix, '\n')

agente_perry = Ornitorrinco(cor_pelo='Verde', cor_bico='Laranja', nro_patas=4,)
print(agente_perry, '\n')