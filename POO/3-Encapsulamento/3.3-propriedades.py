# Com o property() do Python, você pode criar atributos gerenciados em suas classes. Você pode usar atributos gerenciados, também
# conhecidos como propriedades, quando precisar modificar sua implementação interna sem alterar a API pública da classe.


class Foo:
    def __init__(self, x=None):
        self._x = x

    @property # Decoradores são basicamente funções que são executadas antes da função que se encontra abaixo. - coloca um decorador
    def x(self):    # de propriedade nos permitirá acessar este método como se ele fosse um atributo.
        return self._x or 0
    
    @x.setter
    def x(self, valor):
        self._x += valor

    @x.deleter
    def x(self):
        self._x = -1


foo = Foo(10)
print(foo.x)
foo.x = 10

del foo # Deletando x (atribuindo -1)
print(foo.x)