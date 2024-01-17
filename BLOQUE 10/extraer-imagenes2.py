import bs4
import requests
import lxml

resultado = requests.get('https://academiafibonacci.com.gt/')

sopa = bs4.BeautifulSoup(resultado.text, 'lxml')

lista_imagenes = []

for n in range(6):
    imagenes = sopa.select('img')[n]['src']
    lista_imagenes.append('https://academiafibonacci.com.gt/'+imagenes)
    imagen_curso = requests.get(lista_imagenes[n])
    f = open(f"mi_imagen{n}.jpg","wb")
    f.write(imagen_curso.content)
    f.close()

