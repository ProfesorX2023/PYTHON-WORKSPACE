from random import choice
lista_numeros = [1,2,3,4,5,6]

def lanzar_moneda():
    moneda = ["Cara","Escudo"]
    return choice(moneda)

moneda = lanzar_moneda()
def probar_suerte(moneda,lista):
    if moneda == "Cara":
        lista = []
        return f'La lista se autodestruira {lista}'
    elif moneda == "Escudo":
        return f"La lista se salvó {lista}"
    else:
        pass

print(probar_suerte(moneda,lista_numeros))
