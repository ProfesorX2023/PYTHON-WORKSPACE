class Personaje:
    real = False

    def __init__(self, especie, magico, poder):
        self.especie = especie
        self.magico = magico
        self.poder = poder

max = Personaje("Humano",False,"Espadachin")
ken = Personaje("Centauro", False,"Lanza")
tao = Personaje("Elfo",True,"Caer Fuego")

print(f"Max utiliza {max.poder}")
print(f"Ken es un {ken.especie}")
print(f"Tao utiliza {tao.poder}")