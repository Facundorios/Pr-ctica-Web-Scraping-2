from traceback import print_tb
from urllib import response
import requests as rs
from bs4 import BeautifulSoup as bs
import json
import os

# El programa primero válida si la carpeta llamada "imagenes" existe y, de no ser así, se debe crear.


def crear_carpeta():
    try:
        os.makedirs("imagenes")
        print("Carpeta creada.")
    except FileExistsError:
        print("La carpeta ya existe.")
    except OSError as e:
        print(f"Error al crear la carpeta: {e}.")


def obtener_descargar_imgs(url):
    try:
        # Hacemos la petición get a la url, y despues verificamos su estado.
        response = rs.get(url)
        response.raise_for_status()
        # Definimos html, que es el contenido de la página y despues lo parseamos con soup.
        html = response.text
        soup = bs(html, "html.parser")

        # Buscamos todas las etiquetas img y las guardamos en una lista.
        results =  soup.find_all("img")
        img_url = [img['src'] for img in results if 'src' in img.attrs]
        img_url = [img fo img in img_url if re.search(r'')]
        
                
    except (rs.RequestException, rs.exceptions.HTTPError) as e:
        print(f"Error al hacer la petición: {e}")


crear_carpeta()
obtener_descargar_imgs("https://unsplash.com/es/images")
