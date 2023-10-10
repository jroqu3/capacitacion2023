from clase_a import Animal


class Perro(Animal):
    def __init__(self, especie, edad, duenio):
        self.especie = especie
        self.edad = edad
        self.duenio = duenio


mi_perro = Perro("mamífero", 10, "Roque")
print(mi_perro.especie)
print(mi_perro.edad)
print(mi_perro.duenio)
