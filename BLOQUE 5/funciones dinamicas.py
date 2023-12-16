def todos_positivos(lista):
    for n in lista:
        if n >= 0:
            pass
        else:
            return False
    return True

lista_numeros = [1,3,18,-99]



print(todos_positivos(lista_numeros))