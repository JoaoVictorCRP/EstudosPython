#                                                       Método Construtor
# O método construtor sempre é executado quando uma nova instância da classe é criada. Nesse método inicializamos o estado do nosso
# objeto. Para declarar o método construtor da classe, criamos um método com o nome __init__.


#                                                       Método Destrutor
# O método destrutor sempre é executado quando uma instância (objeto) é destruída. Destrutores em Python não são tão necessários
# quanto no C++, por exemplo, pois o Python tem um trash collector que lida com o gerenciamento de memória automaticamente.
# Para declarar o método destrutor da classe, criamos um método com o nome __del__. 


# ¹ - *** métodos que iniciam com Double UNDERline (DUNDER) são chamados "métodos especiais".


# Exemplificando:

class Cachorro:
    def __init__(self, nome, cor, acordado=True) -> None:
        print('Inicializando a classe...')
        self.nome = nome
        self.cor = cor
        self.acordado = acordado
    
    def __del__(self):
        print('Removendo a instância da classe')

    def latir(self):
        if self.acordado == True:
            print('Au, au!')
        else: 
            print(f'{self.nome} está dormindo, não pode latir.')

pet = Cachorro('Jade', 'Caramelo', False)
pet.latir()
# Ao final do código, a destruição do objeto irá ocorrer naturalmente.


# Também podemos forçar a exceução do del

print('Oi, Jade!')
del pet
print('Jade?')
print('Jade??')
print('Jade!!! :(')