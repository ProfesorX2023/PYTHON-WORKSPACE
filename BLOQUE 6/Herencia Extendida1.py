class Padre():
    def trabajar(self):
        print("Trabajando en el hospital")

    def reir(self):
        print("Ja ja ja")

class Madre():
    def trabajar(self):
        print("Trabajando en la fiscalia")

    def reir(self):
        print("Je Je Je")
class Hija(Madre, Padre):
    def jugar(self):
        print("La niña esta jugando")

carmen = Hija()


carmen.trabajar()
carmen.reir()

carmen.jugar()


jorge = Padre()

jorge.trabajar()
jorge.jugar()