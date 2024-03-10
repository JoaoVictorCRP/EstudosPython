#                           Variáveis de Classe VS. Variáveis de Instância

# Todos os objetos nascem o mesmo número de atributos e de instância. Atributos de instância são diferentes para cada objeto, já os
# atributos de classe são compartilhados entre os objetos. VEJA UM EXEMPLO:

class Estudante:
    escola = "DIO" # Atributo de classe - todos os instanciados dessa classe serão da escola "DIO".

    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula # Atributo de instância - Único para cada instância do objeto.

    def __str__(self) -> str:
        return f'{self.nome} - {self.matricula} - {self.escola}'
    
e1 = Estudante('João Victor', 1)
e2 = Estudante('Larissa', 2)

print(e1)
print(e2)

Estudante.escola = 'Python' # Afetará todas as instâncias!

print(e1)
print(e2)