import bs4
import requests
import lxml

resultado = requests.get('https://academiafibonacci.com.gt/')

sopa = bs4.BeautifulSoup(resultado.text, 'lxml')

imagenes = sopa.select('.img-galeria')[0]['src']

#print('https://academiafibonacci.com.gt/'+imagenes)

imagen_curso_1 = requests.get('https://academiafibonacci.com.gt/')

#print(imagen_curso_1.content)

f = open('mi-imagen.jpg', 'wb')
f.write(imagen_curso_1.content)
f.close()