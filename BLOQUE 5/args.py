def suma_cuadrados(*args):
    total = 0
    for arg in args:
        total = arg**2+total
    return total

print(suma_cuadrados(1,2,3,4,5,6))