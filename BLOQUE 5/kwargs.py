def suma(**kwargs):
    total = 0
    for clave,valor in kwargs.items():
        print(f'{clave} es igual a {valor}')
        total = total + valor

    return total

print(suma(x=3,y=5,z=2,a=17,b=-4))
