from clase_a import Animal


class Gato(Animal):
    def hablar(self):
        print("Miau!")

    def moverse(self):
        print("Caminando con 4 patas!")

    def araniar(self):
        print("Arañazo!")


mi_gato = Gato("mamífero", 3)
mi_gato.hablar()
mi_gato.moverse()
mi_gato.araniar()
