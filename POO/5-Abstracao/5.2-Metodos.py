#                                                       Métodos de Classe
# Métodos de classe estão ligados à classe e não ao objeto. Eles têm acesso ao estado da classe, pois recebem um parâmetro que aponta
# para a classe e não para a instância do objeto.


#                                                       Métodos Estáticos
# Um método estático não recebe um primeiro argumento explícito. Ele também é um método vinculado à classe e não ao objeto da classe.
# Ele está presente em uma classe porque faz sentido que o método esteja presente na classe

class Pessoa:
    def __init__(self, nome=None, idade=None):
        self.nome = nome
        self.idade = idade

    @classmethod # Este decorador fará com que a função abaixo seja um método de classe.
    def criar_por_ano_nascimento(cls, nome, ano_nasc):
        idade = 2024 - ano_nasc
        return cls(nome, idade) # cls é uma referência para a classe
    
    @staticmethod
    def e_maior_idade(idade):
        return idade >= 18

p1 = Pessoa('João Victor', 19)
print(p1.nome, p1.idade)

p2 = Pessoa.criar_por_ano_nascimento('Larissa', 1998)
print(p2.nome, p2.idade)

print(Pessoa.e_maior_idade(20))
print(Pessoa.e_maior_idade(8))


# Em suma: 

# CLASS METHOD -> Quando precisamos do contexto da classe

# STATIC METHOD -> Quando o contexto da classe não é necessário.