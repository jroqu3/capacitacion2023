from clase_a import Animal


class Perro(Animal):
    def hablar(self):
        print("Guau!")

    def moverse(self):
        print("Caminando con 4 patas!")


mi_perro = Perro("mamífero", 10)
mi_perro.hablar()
mi_perro.moverse()
