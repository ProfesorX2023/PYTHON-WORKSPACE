class Casa:

    def __init__(self, color, pisos):
        self.color = color
        self.pisos = pisos

casa_blanca = Casa("Blanco", 5)

print(f"Mi casa es color {casa_blanca.color} y tiene {casa_blanca.pisos} pisos")