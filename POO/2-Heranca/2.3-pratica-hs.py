class Veiculo:
    def __init__(self, cor, placa, numero_rodas) -> None:
        self.cor = cor
        self.place = placa
        self.numero_rodas = numero_rodas
        
    def ligar_motor(self) -> None:
        print('Ligando o motor.')

class Motocicleta(Veiculo):
    pass

class Carro(Veiculo):
    pass

class Caminhao(Veiculo):
    def __init__(self,cor, placa, numero_rodas, carregado: bool) -> None:
        self.carregado = carregado

    def esta_carregado(self):
        print(f'{'' if self.carregado else 'Não '}estou carregado')

# moto = Motocicleta('Preta', 'BXZ-450', 2) # Classe filha herda o construtor.
# moto.ligar_motor() # E suas obrigações também.

# carro = Carro('Branco', 'XDE-781', 4)
# carro.ligar_motor()

caminhao = Caminhao('Azul', 'RTE-490', 8, True)
caminhao.ligar_motor()
caminhao.esta_carregado() #

# P: Dá pra usar um metódo de uma classe irmã?
# carro.esta_carregado() R: Por questão de escopo, não!