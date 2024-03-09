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

    def bicar(self):
        print(" 8>> ")


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
    def __init__(self, cor_pelo, cor_bico, nro_patas):
        super().__init__(cor_pelo=cor_pelo, cor_bico=cor_bico, nro_patas=nro_patas)

        print(Ornitorrinco.__mro__) # MRO -> Method Resolution Order, Esse built-in exibe a ordem de busca de métodos no objeto.

    def __str__(self) -> str:
        return __class__.__name__ # MRO na prática - O método __str__ aparece tanto na classe Ornitorrinco quanto na classe avó Animal. Mas, como a classe Ornitorrinco vem
        # Primeiro na ordem, este será o método __str__ que será executado.

#                                                   Instâncias
gato_felix = Gato(cor_pelo='Preto', nro_patas=4) # Lembrando: Quando incluimos kwargs devemos nomear todos os parametros.
print(gato_felix, '\n')

agente_perry = Ornitorrinco(cor_pelo='Verde', cor_bico='Laranja', nro_patas=4)

# Cuidado com a utilização excessiva da herança múltipla, pois quanto maior for uma família de classes, mais complexo, pesado e de difícil manutenibilidade será o código
# Onde ela está inserida!