class Mago():
    def atacar(self):
        print("Ataque mágico")

class Arquero():
    def atacar(self):
        print("Lanzamiento de Flechas")

class Samurai():
    def atacar(self):
        print("Ataque con katana")

musashi = Samurai()
lowe = Mago()
hanz = Arquero()

personajes = [hanz, lowe, musashi]

for personaje in personajes:
    personaje.atacar()