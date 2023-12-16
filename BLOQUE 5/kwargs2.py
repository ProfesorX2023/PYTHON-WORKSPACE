def datos(**kwargs):

    for clave,registro in kwargs.items():
        print(f"{clave} - {registro}")

datos(nombre="Luis",
      edad=19,
      estado="soltero",
      genero="Masculino",
      peso=80.7,
      casaso=False)