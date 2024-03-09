# Como no Python não temos palavras reservadas para definir o nível de acesso a um atributo, como no Java e no C++, nós utilizamos uma
# convenção, que é a utilização de um underline como primeiro caracter para um atributo privado.

# Exemplo com uma classe de conta bancária.

class Conta:
    def __init__(self, nro_agencia:str, saldo:float) -> None:
        self.nro_agencia = nro_agencia
        self._saldo = saldo # Saldo é um atributo privado.(Pelo menos segundo a convenção)

    def depositar(self, valor: float):
        self._saldo += valor

    def sacar(self, valor: float):
        self._saldo -= valor

    def mostrar_saldo(self):
        return self._saldo


conta = Conta('0001',100)
# conta._saldo += 100 # O interpretador não vai levantar uma exception com esta linha, porém fazer uma operação como essa viola a convenção
print(conta.mostrar_saldo())