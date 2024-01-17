import random
import string

def generar_codigo():
    caracteres = string.ascii_uppercase + string.digits
    codigo = ''.join(random.choice(caracteres) for i in range(14))
    return codigo

#generar 100 codigos
codigos = [generar_codigo() for k in range(100)]

for codigo in codigos:
    print(codigo)