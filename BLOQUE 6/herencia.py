class Animal:

    def __init__(self, edad, color):
        self.edad = edad
        self.color = color
    def nacer(self):
        print("Este animal ha nacido")

class Pajaro(Animal):
    pass

piolin = Pajaro(2, "amarillo")

piolin.nacer()

print(piolin.color)
print(piolin.edad)

pajaro_loco = Pajaro(5,"Azul con Naranja")

print(pajaro_loco.color)