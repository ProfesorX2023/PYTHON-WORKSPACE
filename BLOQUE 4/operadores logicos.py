""""a = 6 > 5
b =  30 == 15*3
print(f"Conectivo AND {a and b}")
print(f"Conectivo OR {a or b}")
print(f"Conectivo not { not a }")"""

"""
Imaginen una discoteca de un país desconocido, en esta disco solo pueden ingresar los
mayores de 18 años

1)Como todo país pueden beber los de 18 en adelante

2)Tiene restricción pues no pueden ingresar los mayores de 30

3)Los que tienen 20 y 25 años pueden ingresar grátis

Realice un programa que preguntando la edad le diga si puede tomar, puede entrar, tiene 
entrada grátis

"""

edad = int(input('Escriba su edad: '))
dic = {True:'Si',False:'No'}
print(f"¿puede beber?: {dic[edad >= 18]}")
print(f"¿Puede entrar?: {dic[edad >= 18 and edad <30]}")
print(f"¿Tiene entrada Grátis? {dic[edad == 20 or edad == 25]}")

