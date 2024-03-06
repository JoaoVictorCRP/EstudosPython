class Veiculo:
    def __init__(self, cor, placa, numero_rodas) -> None:
        self.cor = cor
        self.place = placa
        self.numero_rodas = numero_rodas
        
    def ligar_motor(self) -> None:
        print('Ligando o motor.')

    def __str__(self) -> str: # Este método especial será executado quando uma instância do objeto for printada (Stringificada)
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}" # List Comprehension

class Motocicleta(Veiculo):
    pass

class Carro(Veiculo):
    pass

class Caminhao(Veiculo):
    def __init__(self,cor, placa, numero_rodas, carregado: bool) -> None:
        super().__init__(cor, placa, numero_rodas) # Para pegar os atributos da classe pai, utilize super() 
        self.carregado = carregado

    def esta_carregado(self):
        print(f'{'' if self.carregado else 'Não '}estou carregado')

moto = Motocicleta('Preta', 'BXZ-450', 2) # Classe filha herda o construtor.
# moto.ligar_motor() # E suas obrigações também.
carro = Carro('Branco', 'XDE-781', 4)
# carro.ligar_motor()
caminhao = Caminhao('Azul', 'RTE-490', 8, True)#
# caminhao.ligar_motor()
# caminhao.esta_carregado() 
# print(f'A cor do caminhão é {caminhao.cor}') # Caminhão não tem atributo co

print(carro, '\n')
print(moto, '\n')
print(caminhao, '\n')

# P: Dá pra usar um metódo de uma classe irmã?
# carro.esta_carregado() R: Por questão de escopo, não!