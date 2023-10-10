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


class Perro(Animal):
    def hablar(self):
        print("Guau!")

    def moverse(self):
        print("Caminando con 4 patas!")


class Gato(Animal):
    def hablar(self):
        print("Miau!")

    def moverse(self):
        print("Caminando con 4 patas!")

    def araniar(self):
        print("Arañazo!")
