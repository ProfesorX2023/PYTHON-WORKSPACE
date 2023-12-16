def suma_persona(nombre, *args):
    return f"{nombre}, la suma de tus números es {sum(args)}"

print(suma_persona("Carlos",1,2,3,4,5,7,8))