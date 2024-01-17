import numeros

def preguntar():
    print("Bienvenidos a Farmacia Fibonacci")

    while True:
        print("[P] - Perfumeria\n[F] - Farmacia\n[C] - Cosmetica")
        try:
            mi_rubro = input("Elija un rubro").upper()
            ["P","F","C"].index(mi_rubro)
        except ValueError:
            print("Esa opción no es válida")
        else:
            break

    numeros.decorar(mi_rubro)

def inicio():
    while True:
        preguntar()
        try:
            otro_turno = input("¿Quiéres sacar otro turno [S] y [N]?").upper()
        except ValueError:
            print("Esa no es una opción válida")
        else:
            if otro_turno == "N":
                print("Gracias por visitar a farmacia Fibonacci")
                break

inicio()