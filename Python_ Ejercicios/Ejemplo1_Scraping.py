##Ejemplo de realizar un scraping a una página web
import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
    noticias = get_main_news()

# La función get_main_news retornará un diccionario con todas las urls y títulos de noticias encontrados en la sección principal.
def get_main_news():
    url = 'https://www.cmmedia.es/noticias/castilla-la-mancha/'

    respuesta = requests.get(
        url,
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'
        }
    )
