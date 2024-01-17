import bs4
import requests
import lxml

resultado = requests.get('https://academiafibonacci.com.gt/')

#print(type(resultado))

#print(resultado.text)

sopa = bs4.BeautifulSoup(resultado.text, 'lxml')

#print(sopa.select('title'))

#print(sopa.select('p'))

#print(len(sopa.select('p')))

#print(sopa.select('title')[0].getText())

parrafo_especial = sopa.select('p')

print(parrafo_especial[3].getText())