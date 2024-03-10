#                                          Módulo ABC
# Por padrão, o Python não fornece classes abstratas. No entanto, há um módulo que fornece a base para definir as classes abstratas,
# este módulo é o ABC, que funciona decorando métodos da classe base como abstratos, em seguida, registrando classes concretas como
# implementações da base abstrata. Um método se torna abstrato quando decorado com @abstractmethod.

from abc import ABC, abstractmethod, abstractproperty

class ControleRemoto(ABC):
    @abstractmethod # Classes filhas serão obrigadas a implementar a sua própria assinatura de método abstrato.
    def ligar(self):
        pass
    
    @abstractmethod
    def desligar(self):
        pass

    @property
    @abstractproperty # Essa propriedade deverá ser implementada por todas as classes filhas.
    def marca(self):
        pass


class ControleTV(ControleRemoto):
    def ligar(self):
        print('Ligando a TV...')
        print('Ligada!')

    def desligar(self):
        print('Desligando a TV...')
        print('Desligado!')
        
    @property    
    def marca(self):
        return "Samsung"


class ControleArCondicionado(ControleRemoto):
    def ligar(self):
        print('Ligando o Ar Condicionado... ')
        print('Ligado!')

    def desligar(self):
        print('Desligando o Ar Condicionado')
        print('Desligado!')

    @property    
    def marca(self):
        return "Philco"

# controle = ControleTV()
# controle.ligar()
# controle.desligar()
# print(controle.marca)
        
controleAC = ControleArCondicionado()
controleAC.ligar()
print(controleAC.marca)