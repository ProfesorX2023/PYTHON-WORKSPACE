class Libro():
    def __init__(self, titulo, autor, cantidad):
        self.titulo = titulo
        self.autor = autor
        self.cantidad = cantidad

    def __del__(self):
        print("Libro Eliminado")

libro1 = Libro("Cementerio de Mascotas","Stephen King", 1800)

libro1.titulo

