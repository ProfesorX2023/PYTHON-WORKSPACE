class Jugador:
    vivo = True

    @classmethod
    def revivir(cls):
        cls.vivo = False
        print(cls.vivo)

maradona = Jugador()
maradona.revivir()
