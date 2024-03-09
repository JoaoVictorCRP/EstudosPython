# Na herança, a classe filha herda os métodos da classe pai. No entanto, é possível modificar um método em uma classe filha herdada
# da classe pai. Isso é particularmente útil nos casos em que o método herdado da classe pai não se encaixa bem na classe filha.

# Exemplo:

class Passaro:
    def voar(self):
        print('Voando... ')

class Pardal(Passaro):
    def voar(self):
        super().voar()
    
class Avestruz(Passaro):
    def voar(self):
        print(f'{__class__.__name__} não pode voar.')

class Galinha(Passaro):
    def voar(self):
        print(f'{__class__.__name__} não pode voar.')

def hora_de_voar(obj):
    obj.voar()

# p1 = Pardal()
# p2 = Avestruz()
# p3 = Galinha()

hora_de_voar(Pardal())
hora_de_voar(Avestruz())
hora_de_voar(Galinha())