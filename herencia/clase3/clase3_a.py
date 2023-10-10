class Animal:
    def __init__(self, especie, edad):
        self.especie = especie
        self.edad = edad

    def hablar(self):
        pass

    def moverse(self):
        pass

    def describir(self):
        print("Soy un Animal del tipo", type(self).__name__)
