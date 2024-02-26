'''
    O que é herança?
    - Em programação, herança é a capacidade de uma classe filha derivar ou herdar as características de uma calsse pai(base).
    
    Benefícios
    - Fornece reutilização de código, não precisamos escrever o mesmo código repetidamente. Além disso, permite adicionar mais recursos
      a uma classe sem modificá-la
    - É de natureza transitiva, o que significa que, se a classe B herdar da classe A, todas as subclasses de B herdarão automaticamente
      da classe A. [ CUIDADO: NÃO EXAGERE COM CLASSES ANINHADAS]

'''

# Sintaxe:
class A:
    pass

class B(A): #Filha da classe A
    pass