#letras = ['a','b','c','d']
#numeros = [3,6,9,12]

#for letra,numero in zip(letras,numeros):
#    print(letra,numero)

capitales = ["Berlin","Tokio","París","Helsinki","Otawa","Camberra"]

paises = ["Alemania","Japón","Francia","Finlandia","Canadá","Australia"]

combinados=list(zip(capitales,paises))

for capital,pais in combinados:
    print(f"La capital de {pais} es {capital}")