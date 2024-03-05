#                                    Herança Simples
# Quando uma classe filha herda apenas uma classe pai, ela é chamada de herança simples. (como vimos na aula passada)
class A:
    pass

class B(A):
    pass

#                                    Herança Múltipla
# Quando uma classe filha herda de várias classes pai, ela é chamada de herança múltipla.
class A:
    pass

class B:
    pass

class C(A, B):
    pass