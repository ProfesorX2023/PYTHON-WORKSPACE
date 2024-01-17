class Vertebrado:
    vertebrado = True

class Ave(Vertebrado):
    tiene_pico = True
    def poner_huevos(self):
        print("poniendo huevos")

class Reptil(Vertebrado):
    venenoso = True

class Pez(Vertebrado):
    def nadar(self):
        print("Nadando")
    def poner_huevos(self):
        print("Poniendo huevos")

class Mamifero(Vertebrado):
    def caminar(self):
        print("Caminando")
    def amamantar(self):
        print("Amamantando Crías")

class Ornitorrinco(Ave, Reptil, Pez, Mamifero):
    pass

pancho = Ornitorrinco()

print(pancho.vertebrado)

pancho.nadar()
pancho.amamantar()
pancho.caminar()

print(pancho.venenoso)