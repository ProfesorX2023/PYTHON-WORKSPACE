class Pajaro:

    alas = True
    patas = 2

    def __init__(self, color, especie, nombre):
        self.color = color
        self.especie = especie
        self.nombre = nombre



piolin = Pajaro("amarillo","canario", "Piolin")
flopy = Pajaro("negro","cuervo", "Flopy")

#print(f"mi pajaro tiene {flopy.patas} patas y tiene alas {flopy.alas}")
print(f"mi pajaro es un {piolin.especie} y es de color {piolin.color} y se llama {piolin.nombre}")
print(f"mi pajaro es un {flopy.especie} y es de color {flopy.color}")

