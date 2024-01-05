class Libro():
    def __init__(self, titulo, autor, cantidad):
        self.titulo = titulo
        self.autor = autor
        self.cantidad = cantidad

    def __len__(self):
        return self.cantidad

libro1 = Libro("Cementerio de Mascotas","Stephen King", 1800)

print(libro1.titulo)
print(libro1.autor)
print(libro1.cantidad)