def funcion():
    yield "Hola"
    yield "Mamá"
    yield "Estoy Programando"
    yield "Ahora no se que hacer"

variable = funcion()

print(next(variable))
print(next(variable))
print(next(variable))
print(next(variable))
